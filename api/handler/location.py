from fastapi import APIRouter


location_router = APIRouter()


# 게시판 API
@location_router.post("/add")
async def add_location():
    pass
