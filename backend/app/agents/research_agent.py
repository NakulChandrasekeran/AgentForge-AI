
from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="qwen3:1.7b",
    base_url="http://localhost:11434",
    temperature=0,
    num_predict=300,
    reasoning=False,
)


def research_agent(state: dict) -> dict:
    question = state["question"]

    prompt = (
        "You are the Research Agent for AgentForge AI. "
        "Provide a clear, factual answer to the question. "
        "Do not claim to have searched the internet or verified sources. "
        "If uncertain, explain your uncertainty.\n\n"
        f"Question: {question}"
    )

    response = llm.invoke(prompt)

    return {"research": response.content}
