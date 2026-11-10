# MarketLens AI — Phase 1: Original Architecture Decisions

## Phase 1.1 — Functional Requirements

Based on our earlier discussions, here are our initial requirements.

| ID | Functional requirement | Priority |
|---|---|---|
| FR-01 | Retrieve and store historical XAU/USD OHLC candles | Essential |
| FR-02 | Display an interactive TradingView-style candlestick chart | Essential |
| FR-03 | Support multiple timeframes | Essential |
| FR-04 | Calculate technical indicators such as RSI, EMA, MACD, and ATR | Essential |
| FR-05 | Retrieve relevant economic news and events | Essential |
| FR-06 | Execute structured AI market research through LangGraph | Essential |
| FR-07 | Integrate selected market research tools through MCP | Essential |
| FR-08 | Generate and save evidence-backed AI research reports | Essential |
| FR-09 | Backtest strategies using historical data | Essential |
| FR-10 | Train and evaluate experimental ML forecasting models | Essential |
| FR-11 | Display strategy and ML evaluation metrics | Essential |
| FR-12 | Detect and report stale, missing, or invalid market data | Essential |
| FR-13 | Integrate real-time broker market data | Future enhancement |

These are our initial requirements, not yet a finalized specification. We'll refine their exact acceptance criteria during Phase 1.

---

## Phase 1.2 — Architecture Decisions

- Modular Monolith with selective Hexagonal Architecture.
- Historical market data behind a provider interface.
- Provider-specific transformations isolated in adapters.
- Historical ingestion separated from dashboard querying.
- PostgreSQL is our primary local historical-data store.
- Normalized candles include source and quote-type metadata.
- The Technical Analysis Engine depends on normalized data, not provider-specific APIs.
- MT5 can be added later without changing the core candle contract.

These decisions are ready to document in `docs/architecture.md` when we create the repository.

---

## Phase 1.3 — What We've Established

We now have these design decisions:

- Local PostgreSQL will store historical XAU/USD candle data.
- Candles will be identified by their source series, timeframe, quote type, and opening timestamp.
- PostgreSQL will enforce uniqueness.
- Repeated imports must not produce duplicate candle records.
- Historical candle corrections require explicit handling.
- Import operations will produce summaries and track failures.
- Historical data must remain reproducible for backtesting and ML evaluation.

These are ready to be incorporated into `docs/database-design.md` during our documentation work.

---

## Phase 1.4 — Architecture Decisions

- LangGraph orchestrates a bounded, stateful research workflow.
- Python services calculate indicators and retrieve market data.
- The OpenAI model generates interpretations, not authoritative price calculations.
- MCP exposes selected read-only research tools.
- Shared graph state uses validated, typed data.
- Structured reports require schema and factual consistency checks.
- Market-data insufficiency blocks unsupported analysis.
- Optional-source failures can produce explicitly limited reports.
- Execution history, errors, and model costs are recorded locally.
- Automatic live trade execution remains outside the scope.

---

## Phase 1.5 — Architecture Decisions

- Research execution uses a durable background-job architecture.
- FastAPI accepts and validates requests without running the entire workflow in the HTTP handler.
- A separate local worker executes LangGraph.
- PostgreSQL stores the job queue, statuses, and results.
- React initially uses HTTP polling to track execution.
- Workers use atomic claiming and lease-based recovery.
- Research retries are bounded and monitored.
- Final reports are persisted before the job is considered complete.
- We will not introduce Redis, Celery, or microservices unless justified.

---

## Phase 1.6 — Decisions Established

Architecture decisions

- MarketLens AI must remain usable with previously stored historical data when providers fail.
- Stale data must be clearly identified.
- Research freshness depends on timeframe, market session, and source latency.
- Research execution must recover safely from worker failures.
- PostgreSQL must preserve candle integrity and reproducibility.
- Sensitive credentials remain local and are excluded from Git.
- MCP tools initially have read-only permissions.
- Performance, latency, API costs, and errors are measurable.
- We optimize for a reliable single-user local application, not unnecessary distributed infrastructure.

---

## Phase 1.7 — Final Architecture Decisions

Our architecture will be:

**Modular Monolith + Selective Hexagonal Architecture + LangGraph Workflow Orchestration**

### Final Technology Decisions

| Layer | Decision | Status |
|---|---|---|
| Language | Python + TypeScript | Accepted |
| Backend | FastAPI + Pydantic | Accepted |
| Frontend | React + Vite | Accepted |
| Charts | TradingView Lightweight Charts | Accepted, version to verify |
| Database | PostgreSQL + SQLAlchemy + Alembic | Accepted |
| Local infrastructure | Docker Compose | Accepted |
| Historical market data | Python-compatible Dukascopy integration candidate | Proof of concept required |
| Technical analysis | Pandas + NumPy | Accepted |
| AI model integration | OpenAI SDK | Accepted |
| Agent orchestration | LangGraph | Accepted |
| Tool protocol | MCP | Accepted, exact scope deferred |
| Background jobs | Local PostgreSQL-backed worker | Accepted as design; implementation details pending |
| ML | Scikit-learn | Accepted |
| Automated testing | Pytest + Vitest | Accepted |
| Cloud deployment | None | Out of scope |
| Live trade execution | None | Out of scope |

### Phase 1 Review Summary

| Phase | Topic | Assessment |
|---|---|---|
| 1.1 | Functional requirements | Baseline established |
| 1.2 | Market data architecture | Design established |
| 1.3 | Database architecture | Conceptual schema established |
| 1.4 | LangGraph research architecture | Design established |
| 1.5 | Background job architecture | Design established |
| 1.6 | Non-functional requirements | Baseline established |
| 1.7 | Final architecture review | In progress — this review |

### Final Phase 1 Assessment

**Phase 1 — Conceptual design completed**

Ready to begin the local development foundation.

**What we have:** A defined system purpose, high-level architecture, module boundaries, primary data flows, failure policies, initial NFRs, and implementation roadmap.

**What remains:** Convert the approved conceptual decisions into repository documentation, verify technical dependencies, and implement the system progressively.

**Next phase:** Phase 2 — Project Setup & Development Environment.