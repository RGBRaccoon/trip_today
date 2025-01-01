from fastapi import APIRouter, Depends

from core.user_base import fastapi_users, auth_backend, current_active_user
from model.user_model import UserModel
from schema.user_schema import UserCreate, UserRead, UserUpdate

user_router = APIRouter()

user_router.include_router(fastapi_users.get_auth_router(auth_backend), prefix="/jwt")
user_router.include_router(fastapi_users.get_register_router(UserRead, UserCreate))
user_router.include_router(fastapi_users.get_reset_password_router())
user_router.include_router(fastapi_users.get_verify_router(UserRead))
user_router.include_router(fastapi_users.get_users_router(UserRead, UserUpdate))


@user_router.get("/authenticated-route")
async def authenticated_route(user: UserModel = Depends(current_active_user)):
    return {"message": f"Hello {user.email}!"}
