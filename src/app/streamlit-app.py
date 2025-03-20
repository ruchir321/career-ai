JD_FOLDER_PATH = "/home/ruchirich/Documents/repositories/career-ai/data/sample_jd"

# RecursiveCharacterTextSplitter
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

# OllamaEmbeddings
MODEL = "llama3.2"

from typing import List
import os
import dotenv
dotenv.load_dotenv()

# TODO: Fix langsmith tracing
# import getpass
# os.environ["LANGCHAIN_TRACING_V2"] = "true"
# os.environ["LANGCHAIN_API_KEY"] = getpass.getpass()

# os.environ["LANGSMITH_TRACING"] = "true"
# os.environ["LANGSMITH_ENDPOINT"] = "https://api.smith.langchain.com"
# os.environ["LANGSMITH_API_KEY"] = getpass.getpass()
# os.environ["LANGSMITH_PROJECT"] = "career-ai"


# 1. load document, prep model-readable text
from langchain_core.documents import Document
from langchain_community.document_loaders.pdf import PyPDFLoader

# 2. text splitter, break docs into smaller chunks (better for indexing and model context size)
from langchain_text_splitters.character import RecursiveCharacterTextSplitter

# 3.1 embedding, converts text to vectors
from langchain_ollama.embeddings import OllamaEmbeddings
# 3.2 vectorstore, store the vectors( try out a better option MongoDB, Pinecone, Chroma)
from langchain_core.vectorstores import (
    InMemoryVectorStore,
    VectorStore # for type hinting
    )
# 4.1 RAG: retrieve, use VectorStore.as_retriever() function
# 4.2 RAG: generate
from langchain import hub # prompt templates available on langchain hub
from langchain_ollama.chat_models import ChatOllama

# 5. Parse output
from langchain_core.output_parsers.string import StrOutputParser
from langchain_core.runnables.passthrough import RunnablePassthrough

# UI
import streamlit as st

# [ref](https://diptimanrc.medium.com/rapid-q-a-on-multiple-pdfs-using-langchain-and-chromadb-as-local-disk-vector-store-60678328c0df)


def load_split_store() -> VectorStore:
    """
    Load PDF's into a vectorstore.
    Documents are chunks of pdf's
    """

    documents: List[Document] = []

    # load
    for file in os.listdir(JD_FOLDER_PATH):
        file_path = os.path.join(JD_FOLDER_PATH, file)
        loader = PyPDFLoader(
            file_path=file_path
        )

        documents.extend(loader.load())
    
    # split / chunk docs
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        add_start_index=True # metadata for the start character of chunk within the pdf being chunked
    )

    chunked_docs = text_splitter.split_documents(
        documents=documents
    )

    # store in vectorsore
    embedding_model = OllamaEmbeddings(
        model=MODEL
    )

    vectorstore = InMemoryVectorStore.from_documents(
        documents=chunked_docs,
        embedding=embedding_model
    )

    return vectorstore

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)



def get_model_output(query):
    response = rag_chain.invoke(query)
    return response

# ## document retriever

retriever = load_split_store().as_retriever(
    search_type="similarity",
    search_kwargs={"k": 6}
    )

# ## Prompt

prompt = hub.pull("rlm/rag-prompt")

# ## Generate

llm = ChatOllama(
    model=MODEL
)

# ## Chain

rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()} # prepares the two inputs for prompt template
    | prompt # creates a PromptMessage ready for LLM
    | llm # inference
    | StrOutputParser() # just plucks the string content out of the LLM's output message
)


st.set_page_config(
    page_title="career-ai",
    page_icon=":computer:"
)

st.header("What's on your mind?")
form_input = st.text_input("Enter query")
submit = st.button("Generate")

if submit:
    st.write(get_model_output(form_input))
