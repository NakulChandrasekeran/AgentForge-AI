
from datetime import datetime, timezone

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field


from app.workflows.research_graph import research_graph


# Initialize FastAPI application
app = FastAPI(
    title="AgentForge AI",
    description="Enterprise Multi-Agent AI Orchestration Platform",
    version="1.0.0"
)

# -----------------------------------
# CORS Configuration
# -----------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
)


# -----------------------------------
# Home Endpoint
# -----------------------------------

@app.get("/")
def home():
    return {
        "application": "AgentForge AI",
        "message": "Welcome to AgentForge AI Platform",
        "status": "running",
        "version": "1.0.0"
    }


# -----------------------------------
# Health Check Endpoint
# -----------------------------------

@app.get("/health")
def health_check():
    return {
        "status": "success",
        "message": "AgentForge AI backend is running",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }


# -----------------------------------
# Available AI Agents
# -----------------------------------

@app.get("/api/agents")
def get_agents():
    return {
        "agents": [
            {
                "id": 1,
                "name": "Research Agent",
                "status": "active",
                "role": "AI-powered research and information generation"
            },
            {
                "id": 2,
                "name": "Analysis Agent",
                "status": "active",
                "role": "Research analysis and critical evaluation"
            },
            {
                "id": 3,
                "name": "Verification Agent",
                "status": "active",
                "role": "Evidence checking and validation"
            },
            {
                "id": 4,
                "name": "Report Agent",
                "status": "active",
                "role": "Structured report generation"
            }
        ],
        "total_agents": 4,
        "active_agents": 4,
        "planned_agents": 0
    }


# -----------------------------------
# Research Request Model
# -----------------------------------

class ResearchRequest(BaseModel):
    question: str = Field(
        ...,
        min_length=1,
        description="Question to be processed by the AI agents"
    )


# -----------------------------------
# Multi-Agent Research Endpoint
# -----------------------------------



@app.post("/api/research")
def run_research(request: ResearchRequest):
    try:
        result = research_graph.invoke({
            "question": request.question
        })

        return {
            "status": "success",
            "workflow": "Research, Analysis, Verification and Reporting",
            "agents": [
                "Research Agent",
                "Analysis Agent",
                "Verification Agent",
                "Report Agent"
            ],
            "question": request.question,
            "research": result["research"],
            "analysis": result["analysis"],
            "verification": result["verification"],
            "report": result["report"],
            "timestamp": datetime.now(timezone.utc).isoformat()
        }

    except Exception as exc:
        print(f"Multi-agent workflow error: {exc}")

        raise HTTPException(
            status_code=500,
            detail="Multi-agent workflow failed. Check server logs."
        ) from exc
