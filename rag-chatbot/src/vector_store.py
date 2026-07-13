from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

def get_embeddings():
    return HuggingFaceEmbeddings(
        model_name="BAAI/bge-small-en-v1.5"
    )

def create_vector_store(chunks):

    db = Chroma.from_documents(
        documents=chunks,
        embedding=get_embeddings(),
        persist_directory="./chroma_db"
    )

    return db


def load_vector_store():

    db = Chroma(
        persist_directory="./chroma_db",
        embedding_function=get_embeddings()
    )

    return db