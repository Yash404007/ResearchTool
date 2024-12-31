# Research Assistant Tool

This project is a Streamlit-based application designed to assist users in performing research by processing URLs, splitting text, generating embeddings, and enabling question-answering functionality using OpenAI's GPT model. It leverages LangChain for document handling and FAISS for efficient vector storage and retrieval.

---

## Features
- **URL Data Processing**: Extracts and processes content from user-provided URLs.
- **Text Splitting**: Divides content into manageable chunks for analysis.
- **Vector Embeddings**: Generates embeddings for text using OpenAI embeddings.
- **Question Answering**: Enables users to query processed data and receive contextually relevant answers.
- **Sources Display**: Provides sources for answers to ensure transparency and reliability.
- **Error Handling**: Includes mechanisms to manage API quota errors and invalid inputs gracefully.

---

## Requirements

### Python Libraries
- `streamlit`
- `langchain`
- `openai`
- `python-dotenv`
- `faiss-cpu`
- `pickle`
- `time`

### Installation
Install the required libraries using pip:
```bash
pip install streamlit langchain openai python-dotenv faiss-cpu
```

### Environment Variables
Create a `.env` file in the root directory and add your OpenAI API key:
```plaintext
OPENAI_API_KEY=sk-your-openai-api-key
```
Ensure that this file is included in your `.gitignore` to keep your API key secure.

---

## How to Run the Project

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

4. Open the app in your browser using the URL displayed in the terminal (usually `http://localhost:8501`).

---

## Usage

1. **Input URLs**: Use the sidebar to input up to three URLs containing the content you want to research.
2. **Process URLs**: Click the "Process URLs" button to extract and process data from the URLs.
3. **Ask Questions**: Enter your research question in the main text input field. The app will return a contextually relevant answer based on the processed data.
4. **View Sources**: If available, the sources for the answers will be displayed for reference.

---

## Error Handling
- If the OpenAI quota is exceeded, an appropriate error message is displayed, and further API calls are restricted.
- Invalid or empty URLs are handled with user-friendly warnings.

---

## Limitations
- Requires an active OpenAI API key with sufficient quota.
- The accuracy of answers depends on the quality and relevance of the input URLs.

---

## Future Enhancements
- Add support for additional data formats (e.g., PDFs, text files).
- Enable caching to minimize redundant API calls.
- Integrate alternative local embedding models for offline use.

---

## License
This project is licensed under the [MIT License](LICENSE).

---

## Acknowledgements
- [Streamlit](https://streamlit.io/)
- [LangChain](https://langchain.readthedocs.io/)
- [OpenAI API](https://platform.openai.com/docs/)
