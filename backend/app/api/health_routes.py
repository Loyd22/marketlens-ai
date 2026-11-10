from fastapi import APIRouter, Depends

from app.core.database import check_database

router = APIRouter(tags=["Health"])


@router.get("/health")
def health_check() -> dict[str, str]:
    """Check whether the API is responding."""
    return {
        "status": "healthy",
        "service": "marketlens-backend",
    }


@router.get("/health/db")
def database_health_check(
    _: None = Depends(check_database),
) -> dict[str, str]:
    """Check whether the database is reachable."""
    return {
        "status": "healthy",
        "database": "connected",
    }
