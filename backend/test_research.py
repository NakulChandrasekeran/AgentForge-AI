
from app.workflows.research_graph import research_graph

result = research_graph.invoke({
    "question": "What are the benefits and risks of multi-agent AI systems?"
})

print("\n========== RESEARCH AGENT ==========\n")
print(result["research"])

print("\n========== ANALYSIS AGENT ==========\n")
print(result["analysis"])

print("\n========== VERIFICATION AGENT ==========\n")
print(result["verification"])

print("\n========== REPORT AGENT ==========\n")
print(result["report"])

print("\n========== WORKFLOW COMPLETED ==========\n")
