
from app.agents.analysis_agent import analysis_agent
from time import perf_counter

test_state = {
    "question": "What are the benefits and risks of multi-agent AI systems?",
    "research": """
Multi-agent AI systems can improve collaboration,
task distribution, and flexibility.

However, they may introduce coordination problems,
security vulnerabilities, and accountability challenges.

Their effectiveness depends on system design,
communication, and monitoring.
"""
}

start = perf_counter()

result = analysis_agent(test_state)

elapsed = perf_counter() - start

print("\n========== ANALYSIS AGENT ==========\n")
print(result["analysis"])

print("\n========== TEST COMPLETED ==========")
print(f"Execution time: {elapsed:.2f} seconds")
