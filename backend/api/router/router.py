from fastapi import APIRouter

from api.router import user_router

router = APIRouter()

router.include_router(router=user_router, prefix="/auth", tags=["auth"])
