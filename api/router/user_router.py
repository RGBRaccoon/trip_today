from fastapi import Depends, FastAPI

from app.users import auth_backend, current_active_user, fastapi_users

from model.user_model import UserModel
from schema.user_schema import UserCreate, UserRead, UserUpdate

user_router = FastAPI()

user_router.include_router(fastapi_users.get_auth_router(auth_backend), prefix="/auth/jwt", tags=["auth"])
user_router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
user_router.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"],
)
user_router.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["auth"],
)
user_router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)


@user_router.get("/authenticated-route")
async def authenticated_route(user: UserModel = Depends(current_active_user)):
    return {"message": f"Hello {user.email}!"}


@user_router.on_event("startup")
async def on_startup():
    # Not needed if you setup a migration system like Alembic
    await create_db_and_tables()
