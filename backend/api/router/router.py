from fastapi import APIRouter

from api.router.user_router import user_router

main_router = APIRouter()

main_router.include_router(router=user_router, prefix="/auth", tags=["auth"])
