from fastapi import FastAPI

from app.api.health_routes import router as health_router

app = FastAPI(
    title="MarketLens AI API",
    description="Gold (XAU/USD) research and decision-support API",
    version="0.1.0",
)

# Register API routes
app.include_router(health_router)
