
from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="qwen3:1.7b",
    base_url="http://localhost:11434",
    temperature=0,
    num_predict=900,
    reasoning=False,
)


def report_agent(state: dict) -> dict:
    question = state["question"]
    research = state["research"]
    analysis = state["analysis"]
    verification = state["verification"]

    
    prompt = f"""
You are the Report Agent for AgentForge AI.

Create a concise, professional Markdown report.

QUESTION:
{question}

RESEARCH:
{research}

ANALYSIS:
{analysis}

VERIFICATION REVIEW:
{verification}

Write exactly these five sections:

# Research Report

## 1. Executive Summary
Summarize the findings in 2-3 sentences.

## 2. Key Findings
List up to 3 key benefits and 3 key risks.

## 3. Critical Analysis
Summarize the main strengths and limitations
in 3-4 bullet points.

## 4. Verification and Limitations
Identify unsupported claims and uncertainties.
Do not claim independent factual verification.

## 5. Recommendations
Provide 3 practical recommendations.

RULES:
- Keep the entire report under 350 words.
- Do not repeat the same information.
- Do not invent sources, facts, or statistics.
- Preserve uncertainty where evidence is missing.
- Complete all five sections.
"""


    response = llm.invoke(prompt)

    return {
        "report": response.content
    }
