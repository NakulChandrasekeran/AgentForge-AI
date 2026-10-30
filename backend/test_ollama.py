
from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="qwen3:1.7b",
    base_url="http://localhost:11434",
    temperature=0,
    num_predict=200,
    reasoning=False,
)

print("Connecting AgentForge AI to Ollama...")

response = llm.invoke(
    "Explain what an AI research agent does in two short sentences."
)

print("\nAI Response:")
print(response.content)

if not response.content:
    print("Warning: Model returned an empty response.")
