
from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="qwen3:1.7b",
    base_url="http://localhost:11434",
    temperature=0,
    num_predict=400,
    reasoning=False,
)


def analysis_agent(state: dict) -> dict:
    question = state["question"]
    research = state["research"]

    
    prompt = f"""
You are the Analysis Agent for AgentForge AI.

Analyze the Research Agent's response.

QUESTION:
{question}

RESEARCH:
{research}

Provide a concise analysis using exactly
these four sections:

1. Key Findings
Summarize the main findings in 2 sentences.

2. Strengths
List 2 strengths of the research.

3. Limitations and Uncertainties
List 2 limitations or unsupported claims.

4. Practical Implications
Provide 2 actionable recommendations.

RULES:
- Keep the entire response under 180 words.
- Do not invent claims, facts, or sources.
- Only evaluate claims actually present in the research.
- Clearly distinguish evidence from assumptions.
- Complete all four sections.
"""


    response = llm.invoke(prompt)

    return {
        "analysis": response.content
    }
