
from time import perf_counter

from app.agents.verification_agent import verification_agent

test_state = {
    "question": "What are the benefits and risks of multi-agent AI systems?",

    "research": """
Multi-agent AI systems can improve collaboration,
efficiency, and complex task execution.

However, they introduce coordination challenges,
security vulnerabilities, and ethical concerns,
including accountability, privacy, and potential misuse.

These claims are general observations and are not
supported by specific studies in this research.
""",

    "analysis": """
1. Key Findings
Multi-agent systems offer collaboration benefits
but introduce coordination and security risks.

2. Strengths
The research covers both benefits and risks.

3. Limitations and Uncertainties
The research mentions ethical concerns but does
not provide empirical evidence or case studies.

4. Practical Implications
Implement security controls and human oversight.
"""
}

start = perf_counter()

result = verification_agent(test_state)

elapsed = perf_counter() - start

print("\n========== VERIFICATION AGENT ==========\n")
print(result["verification"])

print("\n========== TEST COMPLETED ==========")
print(f"Execution time: {elapsed:.2f} seconds")
