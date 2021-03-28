from typing import Optional

from pydantic import BaseModel


class DailyDataBase(BaseModel):
    id: Optional[int]
    name: Optional[str]
    price: Optional[float]


class DailyDataCreate(DailyDataBase):
    name: str
    price: float


class DailyDataUpdate(DailyDataBase):
    id: int
    pass


class DailyDataResponse(DailyDataBase):
    class Config:
        orm_mode = True
