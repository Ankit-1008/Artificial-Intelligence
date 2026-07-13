# src/document_loader.py

from langchain_community.document_loaders import PyPDFLoader


def load_pdf(pdf_path):
    """
    Loads PDF and returns documents.
    """

    loader = PyPDFLoader(pdf_path)

    documents = loader.load()

    return documents