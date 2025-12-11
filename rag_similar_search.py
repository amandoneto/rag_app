from langchain_core.documents.base import Document
from rag_bot import RAGApplication

class RagApplicationSimilarSearch(RAGApplication):
    """
    A RAG application that only performs similarity search.
    Its only job is to look at the database and return the most relevant documents or text chunks. 
    It does not generate an answer.     What it does: Calculates the similarity between your query 
    and the stored embeddings, returning the top matches.
    Returns: A list of Document objects (raw text + metadata).
    Use case: When you just want to see what information the system finds relevant, 
    without using an LLM to process it.
    No (Free/Fast)
    """
    def _setup(self):
        """
        Sets up the RAG pipeline: loads data, creates embeddings, and builds vector store.
        Skips qa_chain creation.
        """
        docs = self.load_document()

        # 2. Split the document
        splits = self.split_document(docs)

        # 3. Create Vector Store
        self.vector_store = self.create_vector_store(splits)
        
    def search(self, query: str, k: int = 4):
        """
        Search for documents similar to the query.
        
        Args:
            query (str): The query string.
            k (int): Number of documents to return.

        Returns:
            list[Document]: List of similar documents.
        """
        if not self.vector_store:
            return []
        return self.vector_store.similarity_search(query, k=k)

    