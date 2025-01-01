from fastapi import APIRouter


location_router = APIRouter()


# 게시판 API
@location_router.post("/add")
async def add_location():
    pass


@location_router.post("/get")
async def get_location_by_id(id: str):
    pass


@location_router.post("/get/list")
async def get_location_list(lb_x: int, lb_y: int, rt_x: int, rt_y: int, key_word: str):
    """
    _summary_: 사용자가 어떠한 장소를 검색 한 경우 그 검색에 대한 결과값을 리턴.
    _input : 현재 보고 있는 좌표(left_bottom x,y right_top x,y,)
            키워드
            필터링(추가적으로 고려 필요)

    """
    pass
