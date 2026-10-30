
import { useState } from 'react'
import ReactMarkdown from 'react-markdown'
import './App.css'

// -----------------------------------
// AI Agent Configuration
// -----------------------------------

const agents = [
  {
    id: 1,
    name: 'Research Agent',
    icon: '🔎',
    description: 'Research and information gathering',
  },
  {
    id: 2,
    name: 'Analysis Agent',
    icon: '🧠',
    description: 'Critical analysis and insights',
  },
  {
    id: 3,
    name: 'Verification Agent',
    icon: '🛡️',
    description: 'Evidence and consistency review',
  },
  {
    id: 4,
    name: 'Report Agent',
    icon: '📄',
    description: 'Structured research reporting',
  },
]

type AgentTab =
  | 'research'
  | 'analysis'
  | 'verification'
  | 'report'

type ResearchResponse = {
  status: string
  question: string
  research: string
  analysis: string
  verification: string
  report: string
}

// -----------------------------------
// Main Application
// -----------------------------------

function App() {
  const [question, setQuestion] = useState('')
  const [message, setMessage] = useState('')
  const [isLoading, setIsLoading] = useState(false)

  const [research, setResearch] = useState('')
  const [analysis, setAnalysis] = useState('')
  const [verification, setVerification] = useState('')
  const [report, setReport] = useState('')

  const [activeTab, setActiveTab] =
    useState<AgentTab>('report')

  // -----------------------------------
  // Run Multi-Agent Research
  // -----------------------------------

  const handleResearch = async () => {
    if (isLoading) return

    const trimmedQuestion = question.trim()

    if (!trimmedQuestion) {
      setMessage('Please enter a research question.')
      return
    }

    setIsLoading(true)
    setMessage(
      'Your AI agents are processing the research question...'
    )

    setResearch('')
    setAnalysis('')
    setVerification('')
    setReport('')
    setActiveTab('report')

    try {
      const response = await fetch(
        'http://127.0.0.1:8000/api/research',
        {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            question: trimmedQuestion,
          }),
        }
      )

      if (!response.ok) {
        throw new Error(
          `Research request failed: HTTP ${response.status}`
        )
      }

      const data: ResearchResponse =
        await response.json()

      if (
        data.status !== 'success' ||
        typeof data.report !== 'string' ||
        typeof data.research !== 'string' ||
        typeof data.analysis !== 'string' ||
        typeof data.verification !== 'string'
      ) {
        throw new Error(
          'The backend returned an invalid research response.'
        )
      }

      setResearch(data.research)
      setAnalysis(data.analysis)
      setVerification(data.verification)
      setReport(data.report)

      setActiveTab('report')
      setMessage('Research completed successfully!')
    } catch (error) {
      console.error('Research error:', error)

      setMessage(
        error instanceof Error
          ? error.message
          : 'Unable to connect to the research backend.'
      )
    } finally {
      setIsLoading(false)
    }
  }

  // -----------------------------------
  // Download Research Report
  // -----------------------------------

  const handleDownloadReport = () => {
    if (!report) return

    const blob = new Blob([report], {
      type: 'text/markdown;charset=utf-8',
    })

    const url = URL.createObjectURL(blob)
    const link = document.createElement('a')

    link.href = url
    link.download = 'AgentForge-AI-Research-Report.md'

    document.body.appendChild(link)
    link.click()
    document.body.removeChild(link)

    URL.revokeObjectURL(url)
  }

  // -----------------------------------
  // Application Interface
  // -----------------------------------

  return (
    <div className="app-shell">

      {/* Header */}

      <header className="app-header">
        <div className="brand">
          <div className="brand-icon">✦</div>

          <div>
            <h1>AgentForge AI</h1>
            <p>
              Enterprise Multi-Agent Research Platform
            </p>
          </div>
        </div>

        <span className="status-badge">
          ● Local AI Platform
        </span>
      </header>

      <main className="dashboard">

        {/* Welcome */}

        <section className="welcome-section">
          <span className="eyebrow">
            AI RESEARCH WORKSPACE
          </span>

          <h2>
            Research smarter with AI agents.
          </h2>

          <p>
            Four specialized AI agents collaborate to
            research, analyze, review, and generate
            structured reports.
          </p>
        </section>

        {/* Research Input */}

        <section className="panel research-panel">
          <div className="section-heading">
            <div>
              <h3>Start New Research</h3>
              <p>
                Enter a topic or question to begin.
              </p>
            </div>
          </div>

          <label htmlFor="research-question">
            Research Question
          </label>

          <textarea
            id="research-question"
            value={question}
            onChange={(event) =>
              setQuestion(event.target.value)
            }
            placeholder="Example: What are the benefits and risks of multi-agent AI systems?"
            rows={4}
            disabled={isLoading}
          />

          <div className="research-actions">
            <span>
              Powered by Ollama + LangGraph
            </span>

            <button
              type="button"
              onClick={handleResearch}
              disabled={isLoading}
            >
              {isLoading
                ? '⏳ Researching...'
                : '✦ Run Research'}
            </button>
          </div>

          {message && (
            <p
              className="feedback-message"
              role="status"
            >
              {message}
            </p>
          )}
        </section>

        {/* Agent Workflow */}

        <section className="agents-section">
          <div className="section-heading">
            <div>
              <h3>AI Agent Workflow</h3>
              <p>
                Four specialized agents working in sequence.
              </p>
            </div>

            <span className="agent-count">
              4 Agents
            </span>
          </div>

          <div className="agent-grid">
            {agents.map((agent) => (
              <article
                className="agent-card"
                key={agent.id}
              >
                <div className="agent-icon">
                  {agent.icon}
                </div>

                <h4>{agent.name}</h4>

                <p>{agent.description}</p>

                <span className="agent-status">
                  {isLoading
                    ? 'Processing workflow'
                    : report
                      ? 'Completed'
                      : 'Ready'}
                </span>
              </article>
            ))}
          </div>
        </section>

        {/* AI Agent Results */}

        <section className="panel report-panel">
          <div className="section-heading">
            <div>
              <h3>AI Agent Results</h3>

              <p>
                Explore the output generated by each
                specialized AI agent.
              </p>
            </div>
          </div>

          {/* Download Report */}

          {report && (
            <div className="download-actions">
              <button
                type="button"
                className="download-button"
                onClick={handleDownloadReport}
              >
                ↓ Download Report
              </button>
            </div>
          )}

          {/* Agent Result Tabs */}

          {report ? (
            <>
              <div
                className="result-tabs"
                role="tablist"
                aria-label="AI agent results"
              >
                <button
                  type="button"
                  className={
                    activeTab === 'research'
                      ? 'result-tab active'
                      : 'result-tab'
                  }
                  onClick={() =>
                    setActiveTab('research')
                  }
                  role="tab"
                  aria-selected={
                    activeTab === 'research'
                  }
                >
                  🔎 Research
                </button>

                <button
                  type="button"
                  className={
                    activeTab === 'analysis'
                      ? 'result-tab active'
                      : 'result-tab'
                  }
                  onClick={() =>
                    setActiveTab('analysis')
                  }
                  role="tab"
                  aria-selected={
                    activeTab === 'analysis'
                  }
                >
                  🧠 Analysis
                </button>

                <button
                  type="button"
                  className={
                    activeTab === 'verification'
                      ? 'result-tab active'
                      : 'result-tab'
                  }
                  onClick={() =>
                    setActiveTab('verification')
                  }
                  role="tab"
                  aria-selected={
                    activeTab === 'verification'
                  }
                >
                  🛡️ Verification
                </button>

                <button
                  type="button"
                  className={
                    activeTab === 'report'
                      ? 'result-tab active'
                      : 'result-tab'
                  }
                  onClick={() =>
                    setActiveTab('report')
                  }
                  role="tab"
                  aria-selected={
                    activeTab === 'report'
                  }
                >
                  📄 Final Report
                </button>
              </div>

              {/* Formatted Results */}

              <div
                className="report-content"
                role="tabpanel"
              >
                {activeTab === 'research' && (
                  <ReactMarkdown>
                    {research}
                  </ReactMarkdown>
                )}

                {activeTab === 'analysis' && (
                  <ReactMarkdown>
                    {analysis}
                  </ReactMarkdown>
                )}

                {activeTab === 'verification' && (
                  <ReactMarkdown>
                    {verification}
                  </ReactMarkdown>
                )}

                {activeTab === 'report' && (
                  <ReactMarkdown>
                    {report}
                  </ReactMarkdown>
                )}
              </div>
            </>
          ) : (
            <div className="report-empty">
              <div className="report-empty-icon">
                {isLoading ? '⏳' : '📑'}
              </div>

              <h4>
                {isLoading
                  ? 'Your AI agents are working...'
                  : 'No research results yet'}
              </h4>

              <p>
                {isLoading
                  ? 'Research, analysis, verification, and reporting are running. This may take several minutes on your local CPU.'
                  : 'Enter a research question and click Run Research to generate results.'}
              </p>
            </div>
          )}
        </section>
      </main>

      {/* Footer */}

      <footer className="app-footer">
        AgentForge AI · React + TypeScript · FastAPI ·
        LangGraph · Ollama
      </footer>
    </div>
  )
}

export default App
