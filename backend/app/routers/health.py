from fastapi import APIRouter

router = APIRouter(prefix="/api/v1")

@router.get("/health")
def health_check():
    return {"status": "healthy",
            "application": "AI CRM",
            "version": "1.0.0"}