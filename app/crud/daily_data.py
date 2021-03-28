from typing import Optional, List

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.daily_data import DailyData
from app.schemas import DailyDataCreate, DailyDataUpdate


class CRUDTrain(CRUDBase[DailyData, DailyDataCreate, DailyDataUpdate]):
    # Declare model specific CRUD operation methods.
    pass


daily_data = CRUDTrain(DailyData)
