
from langchain_ollama import ChatOllama


# Local Ollama model
llm = ChatOllama(
    model="qwen3:1.7b",
    base_url="http://localhost:11434",
    temperature=0,
    num_predict=400,
    reasoning=False,
)


def verification_agent(state: dict):
    """
    Review the Research and Analysis Agent outputs.

    This agent performs an internal consistency and
    evidence review, not independent fact-checking.
    """

    question = state["question"]
    research = state["research"]
    analysis = state["analysis"]

    prompt = f"""
You are the Verification Agent for AgentForge AI.

Your job is to critically review the Research Agent
and Analysis Agent outputs.

ORIGINAL QUESTION:
{question}

RESEARCH AGENT OUTPUT:
{research}

ANALYSIS AGENT OUTPUT:
{analysis}

Provide a concise verification report with
exactly these five sections:

1. Claims That Appear Reasonable
Identify claims that are consistent with the
supplied text. Do not treat them as proven facts.

2. Claims Lacking Supporting Evidence
Identify claims that need citations, examples,
or independent verification.

3. Contradictions or Inconsistencies
Identify genuine contradictions between the
Research and Analysis outputs.
If none are found, explicitly say so.

4. Uncertainties and Potential Errors
Identify important uncertainties, omissions,
or possible misinterpretations.

5. Recommendations for Further Verification
Suggest practical ways to verify the claims
using reliable external evidence.

IMPORTANT VERIFICATION RULES:
- Check every criticism against the actual
  Research and Analysis text.
- Never claim a topic is missing if it is
  explicitly mentioned.
- Distinguish between a topic being mentioned
  and being supported by evidence.
- Do not attribute an Analysis Agent claim
  to the Research Agent.
- If a claim lacks evidence, describe it as
  unverified, not necessarily false.
- Do not invent facts, sources, or contradictions.
- Do not claim to have independently
  fact-checked information.
- Keep the verification concise and grounded
  in the supplied text.
- Complete all five sections.
- Keep the response under 200 words.
"""

    response = llm.invoke(prompt)

    return {
        "verification": response.content
    }
