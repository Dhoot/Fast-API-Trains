from typing import Optional

from pydantic import BaseModel


class TrainBase(BaseModel):
    id: Optional[int]
    name: Optional[str]
    expected_arrival_time: Optional[str]
    expected_departure_time: Optional[str]


class TrainCreate(TrainBase):
    name: str
    expected_arrival_time: str
    expected_departure_time: str


class TrainUpdate(TrainBase):
    id: int
    pass


class TrainResponse(TrainBase):
    class Config:
        orm_mode = True
