
from rag_bot import RAGApplication
from rag_similar_search import RagApplicationSimilarSearch
import os
import sys

def handle_chat_mode(app, question):
    """
    Handles the chat interaction using the RAG application.
    """
    print("Bot: ", end="", flush=True)
    for chunk in app.ask_stream(question):
        print(chunk, end="", flush=True)
    print() # Newline after stream finishes

def handle_search_mode(app, question):
    """
    Handles the similarity search interaction.
    """
    print(f"\nSearching for documents similar to: '{question}'...\n")
    docs = app.search(question)
    
    if not docs:
        print("No relevant documents found.")
        return

    for i, doc in enumerate(docs):
        print(f"--- Document {i+1} ---")
        print(doc.page_content)
        print("-" * 20)
    print()

def main():

    # Define file path
    pdf_path = os.path.join(os.path.dirname(__file__), "files", "2025_state_of_ai_assisted_software_development.pdf")
    
    print("Select action:")
    print("1. RAG Application (Chat)")
    print("2. Similarity Search")
    
    choice = input("\nEnter choice (1 or 2): ").strip()
    
    if choice == "1":
        print(f"\nInitializing RAG Application (Chat) with {pdf_path}...")
        AppClass = RAGApplication
        handler = handle_chat_mode
    elif choice == "2":
        print(f"\nInitializing Similarity Search with {pdf_path}...")
        AppClass = RagApplicationSimilarSearch
        handler = handle_search_mode
    else:
        print("\nInvalid selection. Please restart and choose 1 or 2.")
        sys.exit(0)

    try:
        app = AppClass(pdf_path)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred during initialization: {e}")
        sys.exit(1)

    print("Application Ready! Type 'exit' or 'quit' to stop.")
    print("-" * 50)

    while True:
        try:
            user_input = input("\nYou: ")
            if user_input.lower() in ["exit", "quit"]:
                print("Goodbye!")
                break
            
            if not user_input.strip():
                continue

            handler(app, user_input)

        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
