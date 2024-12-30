from fastapi import APIRouter


from schema.travel import TravelList
from utils.enum.movement_method import MovementMethod

travel_router = APIRouter()


@travel_router.post("/request", response_model=TravelList)
async def request_travel_by_car(
    method: MovementMethod,
    moving_time,
    total_time,
    meal,
    key_word,
):
    pass
