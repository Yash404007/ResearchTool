from dotenv import load_dotenv
import os
import streamlit as st
import pickle
import time
from langchain import OpenAI
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import UnstructuredURLLoader
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    st.error("OpenAI API key is missing. Please configure your .env file.")
    st.stop()

st.title("Research Tool 📈")
st.sidebar.title("Article URLs")

urls = [st.sidebar.text_input(f"URL {i+1}") for i in range(3)]
process_url_clicked = st.sidebar.button("Process URLs")
file_path = "faiss_store_openai.pkl"
main_placeholder = st.empty()

llm = OpenAI(openai_api_key=api_key, temperature=0.7, max_tokens=20)
cache = {}

if process_url_clicked:
    valid_urls = [url for url in urls if url.startswith("http")]
    if not valid_urls:
        st.error("Please enter at least one valid URL.")
    else:
        try:
            loader = UnstructuredURLLoader(urls=valid_urls)
            main_placeholder.text("Loading data... ✅")
            data = loader.load()

            text_splitter = RecursiveCharacterTextSplitter(separators=["\n\n", "\n", ".", ","], chunk_size=200)
            docs = text_splitter.split_documents(data)
            embeddings = OpenAIEmbeddings(openai_api_key=api_key)
            vectorstore_openai = FAISS.from_documents(docs, embeddings)

            with open(file_path, "wb") as f:
                pickle.dump(vectorstore_openai, f)

            main_placeholder.success("Processing complete!")
        except Exception as e:
            st.error(f"Error: {e}")

query = st.text_input("Question: ")
if query:
    if query in cache:
        st.write(cache[query])
    elif os.path.exists(file_path):
        try:
            with open(file_path, "rb") as f:
                vectorstore = pickle.load(f)
            chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=vectorstore.as_retriever())
            result = chain({"question": query}, return_only_outputs=True)
            cache[query] = result
            st.write(result["answer"])
        except Exception as e:
            if "429" in str(e):
                st.error("Quota exceeded. Please reduce queries or check your plan.")
            else:
                st.error(f"Error: {e}")
    else:
        st.error("No FAISS index found. Please process URLs first.")





