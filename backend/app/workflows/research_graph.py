
from typing import TypedDict

from langgraph.graph import StateGraph, START, END

from app.agents.research_agent import research_agent
from app.agents.analysis_agent import analysis_agent
from app.agents.verification_agent import verification_agent
from app.agents.report_agent import report_agent


class ResearchState(TypedDict):
    question: str
    research: str
    analysis: str
    verification: str
    report: str


# Create workflow
builder = StateGraph(ResearchState)

# Register all four agents
builder.add_node("research_agent", research_agent)
builder.add_node("analysis_agent", analysis_agent)
builder.add_node("verification_agent", verification_agent)
builder.add_node("report_agent", report_agent)

# Define execution sequence
builder.add_edge(START, "research_agent")
builder.add_edge("research_agent", "analysis_agent")
builder.add_edge("analysis_agent", "verification_agent")
builder.add_edge("verification_agent", "report_agent")
builder.add_edge("report_agent", END)

# Compile workflow
research_graph = builder.compile()
