# AI-based Question Answering System (LangGraph Multi-Agent)

This project is an advanced AI-based question answering system implemented using LangGraph. It automates the process of planning, researching, generating answers, and reflecting on complex questions by combining multiple AI agents.

## Key Features

- Question analysis and response planning
- Related information research and collection
- Answer generation and improvement
- Reflection and critique of generated answers

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/Eric-Kim-HY/langgraph-essay-writer
   cd langgraph-essay-writer
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Create a `.env` file and set all the necessary environment variables:
   ```
   AZURE_OPENAI_API_VERSION=your_azure_openai_api_version
   AZURE_OPENAI_MODEL_NAME=your_azure_openai_model_name
   AZURE_OPENAI_ENDPOINT=your_azure_openai_endpoint
   AZURE_OPENAI_API_KEY=your_azure_openai_api_key
   ```

## Usage

1. Run the main script:
   ```
   python main.py
   ```

2. Enter your question when prompted.

3. Observe the system processing the question and generating an answer.

## Project Structure

- `main.py`: Main execution script
- `agents/`: Modules containing logic for each AI agent
- `models/`: State and data model definitions
- `utils/`: Utility functions and prompts
- `config.py`: Configuration file
