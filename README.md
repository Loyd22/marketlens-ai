# MarketLens AI

**AI-Powered Gold (XAU/USD) Trading Research & Decision Support System**

## Overview

MarketLens AI is a personal-use, locally hosted research and decision-support application for Gold (XAU/USD). It is being developed incrementally as a complete, maintainable trading research platform and as an AI/software engineering portfolio project.

The planned system brings together historical market data, technical indicators, economic news, evidence-backed AI research, strategy backtesting, and machine learning experiments. It supports informed decisions; **it does not execute live trades automatically**.

**Current development status:** Phase 2 — Development foundation implemented and locally verified; final README/Git milestone in progress. Phase 3 — Database Design & Persistence is next.

> **Implemented vs. planned:** The current application provides a working FastAPI backend, React/Vite frontend, local PostgreSQL infrastructure, and a basic database connectivity check. The trading and AI features described below are **not implemented yet**.

## Planned Features

- Import and store historical XAU/USD OHLC candles from a verified provider.
- Display interactive candlesticks with multiple timeframes using TradingView Lightweight Charts.
- Calculate deterministic technical indicators: RSI, EMA, SMA, MACD, ATR, and market-structure signals.
- Retrieve economic news and events relevant to gold (including US CPI, NFP, and Federal Reserve announcements).
- Orchestrate structured, evidence-backed research with LangGraph and the OpenAI API.
- Expose approved, read-only research capabilities via MCP.
- Persist AI research jobs, reports, execution status, and relevant diagnostic information.
- Backtest trading strategies using reproducible historical data and realistic execution assumptions.
- Experiment with ML price forecasts using chronological validation and baseline comparisons.
- Detect stale, incomplete, missing, or invalid market data.

**Future enhancement:** Optional real-time broker data (potentially MetaTrader 5). Automated live trade execution is out of scope.

## Technology Stack

| Layer | Technology | State |
|---|---|---|
| Frontend | React, TypeScript, Vite | Phase 2 foundation implemented |
| Frontend quality | ESLint, Vitest, Testing Library | Phase 2 foundation implemented |
| Charting | TradingView Lightweight Charts | Planned — Phase 5 |
| Backend | Python 3.12, FastAPI, Pydantic | Phase 2 foundation implemented |
| Backend quality | Pytest, Ruff | Phase 2 foundation implemented |
| Database | PostgreSQL 16, Docker Compose | Phase 2 infrastructure implemented |
| Database access | SQLAlchemy 2, psycopg | Initial connection layer in Phase 2 |
| Database migrations | Alembic | Planned — Phase 3 |
| Quantitative analysis | Pandas, NumPy | Planned — Phase 6 |
| AI model integration | OpenAI API | Planned — Phase 8 |
| AI orchestration | LangGraph | Planned — Phase 9 |
| Tool integration | MCP | Planned — Phase 10 |
| Machine learning | Scikit-learn | Planned — Phase 12 |

Dependency ranges are declared in `backend/pyproject.toml` and the frontend's `package.json`. Exact resolved versions may change when dependencies are installed or updated; see the respective local environment and `frontend/package-lock.json`.

## Architecture

MarketLens AI follows a **Modular Monolith with Selective Hexagonal Architecture (Ports and Adapters)**. The application is developed as one backend codebase with modules organized by business responsibility. Interfaces are introduced primarily where external dependencies may change, especially historical market data providers.

Planned domain modules:

- Market Data
- Technical Analysis
- Economic News
- AI Research
- MCP Integration
- Backtesting
- ML Forecasting
- Reporting

### Planned Market Data Flow

```text
External Provider
    → Provider Adapter
    → Normalization & Validation
    → Candle Repository
    → PostgreSQL
    → Query Service
    → FastAPI
    → React
```

Historical ingestion and dashboard queries will be separate processes. Data will retain source/series identity, quote type, timeframe, timestamp, and quality metadata to support integrity and reproducibility.

### Planned AI Research Flow

```text
React research request
    → FastAPI validation
    → PostgreSQL-backed job
    → Local Python worker
    → LangGraph research workflow
    → Evidence assembly & deterministic calculations
    → Structured AI interpretation & validation
    → Persist report
    → React polls job status/results
```

Research execution will use bounded retries, atomic job claiming, and recovery mechanisms. The OpenAI model will interpret verified evidence, not act as the authoritative calculator for prices or indicators.

### Current Phase 2 Connectivity Flow

```text
React (localhost:5173)
    → HTTP GET /health/db
    → FastAPI (127.0.0.1:8000)
    → SQLAlchemy + psycopg
    → PostgreSQL (127.0.0.1:5435)
    → SELECT 1
    → JSON status to React
```

`GET /health` checks whether the API responds; `GET /health/db` checks database connectivity. The latter returns a failure status when PostgreSQL is unavailable.

## Design Principles

1. Build a reliable **localhost-only**, single-user application rather than unnecessary distributed infrastructure.
2. Keep deterministic market calculations and financial rules in tested Python code.
3. Use AI for grounded research interpretation with validated structured outputs.
4. Preserve market-data provenance, timestamps, quote types, freshness, and quality.
5. Make imports idempotent and historical analyses reproducible.
6. Recover research jobs safely after worker failure; impose limits on retries and costs.
7. Keep secrets in local environment variables, never in committed source code.
8. Prefer maintainability, observability, and appropriate risk-based tests over premature complexity.
9. Keep MCP research tools read-only by default.
10. Exclude automated live trade execution from the project scope.

## Local Development Setup

The Phase 2 foundation was developed on Windows 11 using Python 3.12, Node.js 22, Docker Desktop with WSL2, Git, and VS Code. It runs **locally**, even though the GitHub repository can be public.

### Prerequisites

- Python 3.12
- Node.js 22 and npm
- Docker Desktop with Linux containers / WSL2
- Git

### 1. Clone the project

```powershell
git clone https://github.com/Loyd22/marketlens-ai.git
cd marketlens-ai
```

### 2. Configure and start PostgreSQL

From the project root, create your private database environment file:

```powershell
Copy-Item .env.example .env
```

Edit `.env` to set your own strong local PostgreSQL password. The Phase 2 Compose configuration expects:

```dotenv
POSTGRES_DB=marketlens
POSTGRES_USER=marketlens_user
POSTGRES_PASSWORD=replace_with_your_own_local_password
```

Start the database:

```powershell
docker compose up -d
```

| Service | Local address |
|---|---|
| PostgreSQL 16 | `127.0.0.1:5435` |

Docker stores database files in its **named volume** (`marketlens_postgres_data`). A persistent volume does not replace a backup; database backup and restore procedures will be developed in Phase 3.

> Changing `POSTGRES_USER`, `POSTGRES_DB`, or `POSTGRES_PASSWORD` after the volume is initialized does not automatically reconfigure the existing database. Do not delete the volume to change credentials without understanding the data-loss risk.

### 3. Start the FastAPI backend

Open a second PowerShell terminal:

```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e ".[dev]"
python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

Backend settings load the database variables from the project-root `.env`, with local defaults for host `127.0.0.1` and port `5435`.

| Endpoint | Purpose |
|---|---|
| `http://127.0.0.1:8000/health` | API process health |
| `http://127.0.0.1:8000/health/db` | Database connectivity |
| `http://127.0.0.1:8000/docs` | FastAPI interactive API documentation |

### 4. Start the React frontend

Open a third PowerShell terminal:

```powershell
cd frontend
npm ci
Copy-Item .env.example .env.local
npm run dev
```

The example frontend configuration is:

```dotenv
VITE_API_BASE_URL=http://127.0.0.1:8000
```

Open `http://localhost:5173`. The current interface is a small **development connectivity screen**, not the planned TradingView dashboard. It displays whether the backend can connect to PostgreSQL.

**Security note:** Vite variables prefixed with `VITE_` are exposed to the browser. Never put passwords or API keys in them.

### 5. Run quality checks

From `backend/` with its virtual environment active:

```powershell
python -m ruff check .
python -m ruff format --check .
python -m pytest -q
```

From `frontend/`:

```powershell
npm run lint
npm run test
npm run build
```

These checks were reported passing at the conclusion of Phase 2 implementation; rerun them after changing dependencies or code. The initial automated tests cover basic API health and frontend connectivity behavior, not the planned trading features.

### 6. Stop local services

Stop the FastAPI and Vite development servers using `Ctrl + C` in their terminals. From the project root:

```powershell
docker compose stop
```

Start PostgreSQL again with `docker compose start` or `docker compose up -d`.

**Avoid `docker compose down -v`** unless intentionally deleting the PostgreSQL volume and all its data.

## Project Structure

The project is evolving. Relevant foundation paths after Phase 2:

```text
marketlens-ai/
├── .github/
│   └── workflows/                # Reserved for future workflows
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   └── health_routes.py
│   │   ├── core/
│   │   │   ├── config.py
│   │   │   └── database.py
│   │   └── main.py
│   ├── tests/
│   └── pyproject.toml
├── frontend/
│   ├── src/
│   │   ├── services/
│   │   │   └── healthApi.ts
│   │   ├── test/
│   │   │   └── setup.ts
│   │   ├── App.test.tsx
│   │   └── App.tsx
│   ├── package.json
│   ├── package-lock.json
│   └── vite.config.ts
├── docs/
│   └── phase-1-architecture-decisions.md
├── compose.yaml
├── .env.example
├── .gitignore
└── README.md
```

Additional modules, persistence models, migrations, and tests will be added in the phases that require them. Local `.env` files, virtual environments, `node_modules`, and database volumes are not committed.

## Development Roadmap

MarketLens AI is a **15-phase project**. The roadmap is the development baseline, with implementation details refined through testing and evidence.

| Phase | Name | Scope | Status |
|---|---|---|---|
| 01 | Requirements & System Design | Define functionality, architecture, module responsibilities, data flows, functional/non-functional requirements, and acceptance criteria. | Completed |
| 02 | Project Setup & Development Environment | Establish Git, FastAPI, React, TypeScript, Docker, local PostgreSQL, environment configuration, linting, and automated testing. | Completed |
| 03 | Database Design & Persistence | Design tables, relationships, constraints, indexes, repositories, Alembic migrations, and local database backups. | Planned |
| 04 | Market Data Integration | Integrate free historical XAU/USD data; validate and normalize candles; handle failures and persist reliable data. | Planned |
| 05 | TradingView-Style Dashboard | Build interactive gold candlesticks, timeframes, market overview, chart navigation, and freshness indicators. | Planned |
| 06 | Technical Analysis Engine | Implement deterministic RSI, EMA, SMA, MACD, ATR, trends, and support/resistance. | Planned |
| 07 | Economic News & Market Context | Integrate gold-related news, US CPI, NFP, Fed events, and macro context. | Planned |
| 08 | AI Research Foundation | Integrate OpenAI API, structured outputs, schemas, prompts, evidence handling, validation, and errors. | Planned |
| 09 | LangGraph Research Workflow | Implement stateful nodes, edges, tools, checkpointing, background jobs, retries, and recovery. | Planned |
| 10 | MCP Tool Integration | Create controlled read-only tools for market data, indicators, news, and approved research functions. | Planned |
| 11 | Strategy Backtesting Engine | Simulate historical trades with entry/exit rules, stops, targets, spread, slippage, and performance analytics. | Planned |
| 12 | ML Forecasting & Evaluation | Train and evaluate models using chronological splits, baselines, and walk-forward validation. | Planned |
| 13 | AI Reports & Dashboard Integration | Connect research workflows, indicators, news, ML, and backtesting to React. | Planned |
| 14 | Testing, AI Evaluations & Local Operations | Perform integration tests, AI evals, security reviews, performance checks, recovery, logging, monitoring, and backup testing. | Planned |
| 15 | Final Documentation & Portfolio | Finalize README, architecture/API docs, user guide, test reports, demo materials, and final acceptance. | Planned |

### Development Workflow

**Requirements → Inspect → Design → Implement → Targeted Tests → Debug → Review Diff → Document → Commit & Push**

Before moving to a new phase:

1. Check the phase's risk-appropriate acceptance criteria.
2. Run applicable automated tests and review material correctness/security risks.
3. Update the README and relevant engineering documentation.
4. Commit and push the verified changes to GitHub.

This README is updated at each completed phase to reflect **what actually exists**, not merely what was planned.

## Security and Operational Boundaries

- The application remains **localhost-only**, regardless of the repository's GitHub visibility.
- No public cloud deployment or automatic live trading is planned.
- API keys and local database passwords must remain outside Git.
- Use placeholder values in `.env.example` files.
- PostgreSQL data persists locally; backup and restore validation is planned for Phase 3.
- MCP tools will initially be read-only.
- Historical/delayed market data is acceptable at the start; paid real-time feeds are optional future enhancements.
- Research reports must disclose insufficient or stale market evidence.

## Architecture Documentation

See [Phase 1 Architecture Decisions](docs/phase-1-architecture-decisions.md) for the conceptual architecture baseline.

## Disclaimer

MarketLens AI is a trading research and decision-support application. Its calculations, forecasts, and AI-generated reports are not guarantees of future market performance or financial outcomes.
