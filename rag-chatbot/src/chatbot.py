from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate


def format_docs(docs):
    """
    Cleanly format retrieved documents
    """
    return "\n\n".join(
        f"Source {i+1}:\n{doc.page_content}"
        for i, doc in enumerate(docs)
    )


def generate_answer(question, docs):

    # Step 1: Prepare context
    context = format_docs(docs)

    # Step 2: Prompt template (better structured)
    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template="""
You are a highly accurate AI assistant.

Use ONLY the context below to answer the question.
If the answer is not in the context, say: "I don't know based on the provided documents."

----------------
Context:
{context}
----------------

Question:
{question}

Answer clearly and concisely:
"""
    )

    final_prompt = prompt.format(
        context=context,
        question=question
    )

    # Step 3: LLM (still OpenAI, can be replaced later)
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0
    )

    response = llm.invoke(final_prompt)

    return response.content