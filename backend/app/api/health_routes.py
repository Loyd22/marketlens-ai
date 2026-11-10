from fastapi import APIRouter

router = APIRouter(tags=["Health"])


@router.get("/health")
def health_check() -> dict[str, str]:
    """Check whether the API is responding."""
    return {
        "status": "healthy",
        "service": "marketlens-backend",
    }
