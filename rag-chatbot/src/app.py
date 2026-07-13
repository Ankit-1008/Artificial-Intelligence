import os
import tempfile
import streamlit as st

from dotenv import load_dotenv

from src.document_loader import load_pdf
from src.text_splitter import split_documents
from src.vector_store import create_vector_store
from src.vector_store import load_vector_store
from src.chatbot import generate_answer


load_dotenv()

st.set_page_config(
    page_title="RAG Chatbot",
    page_icon="🤖"
)

st.title("📚 RAG Chatbot")

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file:

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    ) as tmp_file:

        tmp_file.write(uploaded_file.read())

        pdf_path = tmp_file.name

    with st.spinner("Processing PDF..."):

        docs = load_pdf(pdf_path)

        chunks = split_documents(docs)

        create_vector_store(chunks)

    st.success("PDF Processed Successfully!")

question = st.text_input(
    "Ask a question about the PDF"
)

if question:

    db = load_vector_store()

    retriever = db.as_retriever(
        search_kwargs={"k": 4}
    )

    retrieved_docs = retriever.invoke(question)

    answer = generate_answer(
        question,
        retrieved_docs
    )

    st.subheader("Answer")

    st.write(answer)

    st.subheader("Sources")

    for doc in retrieved_docs:
        st.write(
            f"Page: {doc.metadata.get('page', 'Unknown')}"
        )