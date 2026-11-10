# MarketLens AI

**AI-Powered Gold (XAU/USD) Trading Research & Decision Support System**

## Overview

MarketLens AI is a personal-use trading research platform designed to support evidence-based analysis of Gold (XAU/USD).

The application will combine historical market data, technical analysis, economic news, AI-assisted research, backtesting, and machine learning experiments into a unified dashboard.

The goal is to build a reliable, maintainable research system that supports informed trading decisions without automatically executing live trades.

**Project status:** Phase 2 — Project Setup & Development Environment.

## Planned Features

- Historical XAU/USD market data ingestion and storage
- Interactive candlestick charts with multiple timeframes
- Technical indicators including RSI, EMA, MACD, and ATR
- Market structure and trend analysis
- Economic news and event research
- LangGraph-based AI research workflows
- Read-only research tools using MCP
- Structured, evidence-backed AI research reports
- Persistent background research jobs
- Historical strategy backtesting
- Experimental ML price forecasting and evaluation
- Data freshness, quality, and source tracking

These features are planned and will be implemented incrementally.

## Technology Stack

| Layer | Technology |
|---|---|
| Frontend | React, TypeScript, Vite |
| Charting | TradingView Lightweight Charts |
| Backend | Python, FastAPI, Pydantic |
| Database | PostgreSQL |
| ORM & Migrations | SQLAlchemy, Alembic |
| Infrastructure | Docker Compose |
| Market Analysis | Pandas, NumPy |
| AI Integration | OpenAI API |
| AI Orchestration | LangGraph |
| Tool Integration | MCP |
| Machine Learning | Scikit-learn |
| Backend Testing | Pytest |
| Frontend Testing | Vitest |
| Python Linting | Ruff |

Exact dependency versions will be verified during development.

## Architecture

MarketLens AI follows a **Modular Monolith with Selective Hexagonal Architecture**.

The backend will be organized into independent functional modules while remaining part of one application.

Primary modules:

- Market Data
- Technical Analysis
- Economic News
- AI Research
- MCP Integration
- Backtesting
- ML Forecasting
- Reporting

Ports and adapters will be used where external dependencies justify abstraction, particularly market data providers.

### Market Data Flow

External Provider → Provider Adapter → Data Normalization & Validation → PostgreSQL → Query Service → FastAPI → React

Historical ingestion will be separated from dashboard queries.

### AI Research Flow

Research Request → FastAPI → PostgreSQL Job Queue → Local Worker → LangGraph Workflow → Validated Research Report → PostgreSQL

React will initially monitor research progress through HTTP polling.

## Design Principles

1. Keep the application local-first and suitable for a single user.
2. Use deterministic Python calculations for technical indicators and numerical analysis.
3. Use AI for research interpretation, not authoritative financial calculations.
4. Preserve the source, timestamps, quality, and identity of market data.
5. Design background jobs for safe retries, recovery, and idempotency.
6. Validate AI outputs before using or persisting them.
7. Protect API keys and credentials using environment-based configuration.
8. Keep infrastructure simple unless complexity is justified.
9. Prioritize testing, reproducibility, monitoring, and maintainability.
10. Do not implement automatic live trade execution.

## Development Environment

The application is intended to run locally on Windows using:

- Python 3.12
- Node.js 22
- Docker Desktop with WSL2
- PostgreSQL through Docker Compose
- Git and VS Code

The exact local startup procedure will be documented after the backend, frontend, and database have been initialized.

## Project Structure

```text
marketlens-ai/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   └── core/
│   └── tests/
├── frontend/
├── docs/
│   └── phase-1-architecture-decisions.md
├── .github/
│   └── workflows/
├── .gitignore
└── README.md
```

Additional directories will be introduced when their functionality is implemented.

## Development Roadmap

MarketLens AI follows a structured, 15-phase development roadmap. Each phase focuses on a specific engineering responsibility, allowing the system to grow incrementally into a complete, maintainable, personal-use trading research platform.

| Phase | Name | Description | Status |
|---|---|---|---|
| 01 | Requirements & System Design | Define functionality, system architecture, module responsibilities, data flow, functional and non-functional requirements, and acceptance criteria. | Completed |
| 02 | Project Setup & Development Environment | Initialize Git, FastAPI, React, TypeScript, Docker, local PostgreSQL, environment variables, linting, and automated testing. | In Progress |
| 03 | Database Design & Persistence | Design database tables, relationships, constraints, indexes, repositories, Alembic migrations, and local database backups. | Planned |
| 04 | Market Data Integration | Integrate free historical XAU/USD data, validate and normalize OHLC candles, handle provider failures, and persist reliable market data. | Planned |
| 05 | TradingView-Style Dashboard | Build an interactive gold candlestick chart with timeframe selection, market overview, chart navigation, and data freshness indicators. | Planned |
| 06 | Technical Analysis Engine | Implement RSI, EMA, SMA, MACD, ATR, market trends, and support/resistance calculations using deterministic Python. | Planned |
| 07 | Economic News & Market Context | Integrate gold-related financial news, US CPI, NFP, Federal Reserve events, and other relevant macroeconomic information. | Planned |
| 08 | AI Research Foundation | Integrate the OpenAI API, structured outputs, research schemas, prompt design, evidence handling, validation, and error handling. | Planned |
| 09 | LangGraph Research Workflow | Build the stateful AI research workflow with nodes, edges, tools, checkpointing, background execution, retries, and recovery. | Planned |
| 10 | MCP Tool Integration | Create controlled, read-only MCP tools for market data, technical indicators, news retrieval, and other approved research operations. | Planned |
| 11 | Strategy Backtesting Engine | Build a historical trading simulator with entry/exit rules, stop-loss, take-profit, spread, slippage, and performance analytics. | Planned |
| 12 | ML Forecasting & Evaluation | Train and evaluate machine learning models for gold market forecasting using chronological splits, baselines, and walk-forward validation. | Planned |
| 13 | AI Reports & Dashboard Integration | Connect LangGraph research, technical indicators, news, ML results, and backtesting to the complete React trading dashboard. | Planned |
| 14 | Testing, AI Evaluations & Local Operations | Perform integration tests, AI evaluations, security reviews, performance measurements, failure recovery, logging, monitoring, and backup testing. | Planned |
| 15 | Final Documentation & Portfolio | Complete README, architecture diagrams, API documentation, user instructions, test reports, demo materials, and final acceptance testing. | Planned |

### Development Workflow

Each phase follows a consistent engineering process:

**Requirements → Inspection → Design → Implementation → Testing → Debugging → Code Review → Documentation → Git Commit & Push**

Before proceeding to the next development phase:

1. Verify that the phase's acceptance criteria are satisfied.
2. Run the applicable automated tests and quality checks.
3. Review code changes for correctness, maintainability, and security.
4. Update project documentation and `README.md`.
5. Commit and push the verified changes to GitHub.

The roadmap defines the development sequence, but implementation details may be refined as technical constraints and testing results become clearer.

**Current milestone:** Phase 2 — Project Setup & Development Environment.

## Security and Operational Boundaries

- Localhost-only hosting
- No public cloud deployment
- No automated live trading
- API keys excluded from Git
- PostgreSQL persisted using local Docker storage
- MCP research tools initially read-only
- Free historical or delayed data initially
- Optional real-time broker data integration in the future

## Architecture Documentation

See [Phase 1 Architecture Decisions](docs/phase-1-architecture-decisions.md) for the complete conceptual design baseline.

## Disclaimer

MarketLens AI is a research and decision-support application. Its analysis, forecasts, and AI-generated reports are not guarantees of market performance or financial outcomes.