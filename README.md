# RAG Chat Application

## Description
This is a Retrieval Augmented Generation (RAG) command-line application designed to process and chat with a local PDF document. It leverages LangChain and OpenAI to answer user questions based on the content of the "2025 State of AI-Assisted Software Development" report.

## Goal
- The goal of this application is to demonstrate a local RAG implementation that reads a specific annual report about Dora report ("2025_state_of_ai_assisted_software_development.pdf") and allows users to query it interactively. The report can be downloaded from https://dora.dev/research/2025/dora-report/
and place the report under files folder

- The 2025 DORA Report, now retitled the State of AI-Assisted Software Development, reveals that artificial intelligence acts as an amplifier rather than a universal solution—magnifying efficiency in organizations with strong engineering foundations while increasing instability and "toil" in those with existing bottlenecks. While the report finds near-universal AI adoption (approximately 90%), it identifies a critical "trust paradox" where many developers rely on code generation tools they do not fully trust, shifting the industry's focus from simple speed metrics toward platform engineering, robust internal data quality, and human-centric developer experience as the primary drivers of success. In a significant departure from previous years, the 2025 study replaces the traditional "Elite through Low" performance clusters with seven distinct team archetypes (such as "Harmonious High-Achievers" vs. "Legacy Bottlenecks") to provide a more nuanced framework for diagnosing how AI interacts with team culture and organizational health.

## Key Components

The application offers two modes of operation, chosen at runtime:

1.  **RAGApplication**: The standard RAG pipeline. It retrieves relevant documents and uses an LLM (OpenAI) to generate a natural language answer to the user's question. This mode provides a full chat experience.
2.  **RagApplicationSimilarSearch**: A lightweight mode that only performs the similarity search step. It retrieves and displays the raw text chunks from the PDF that match the user's query, without passing them to an LLM. This is useful for debugging retrieval or inspecting source data directly without incurring LLM costs.

## Dependencies
This project is managed using `uv`. The key dependencies are:
- `langchain`: Framework for developing applications powered by language models.
- `langchain-openai`: OpenAI integration for LangChain.
- `langchain-community`: Community maintained integrations.
- `langchain-core`: Core LangChain abstractions.
- `pypdf`: For loading PDF documents.
- `faiss-cpu`: For efficient vector similarity search.
- `tiktoken`: Tokenizer for OpenAI models.
- `python-dotenv`: For managing environment variables.

## Prerequisites
- **Python**: Version 3.12 or higher.
- **OPENAI_API_KEY**: You must have a valid OpenAI API key in your `.env` file.
- **OPENAI_MODEL_NAME**: You must specify the OpenAI model name (e.g., `gpt-4o`) in your `.env` file.

## Setup & Usage

1. **Clone/Navigate to the directory**:
   Ensure you are in the project root.

2. **Environment Variables**:
   Create a `.env` file in the root directory (if not already present) and add your OpenAI API key:
   ```env
   OPENAI_API_KEY=sk-your-api-key-here
   OPENAI_MODEL_NAME=your-favorite-openai-model
   ```

3. **Install Dependencies**:
   Using `uv`, you can sync the project:
   ```bash
   uv sync
   ```

4. **Run the Application**:
   Execute the `main.py` script:
   ```bash
   uv run main.py
   ```

5. **Interact**:
   - Type your questions when prompted with `You:`.
   - Type `exit` or `quit` to close the application.
