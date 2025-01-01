from typing import List
from pydantic import BaseModel


class Travel(BaseModel):
    pass


class TravelList(BaseModel):
    Travel_list = List[Travel]
