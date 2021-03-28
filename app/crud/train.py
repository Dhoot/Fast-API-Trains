from typing import Optional, List

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.train import Train
from app.schemas import TrainCreate, TrainUpdate


class CRUDTrain(CRUDBase[Train, TrainCreate, TrainUpdate]):
    # Declare model specific CRUD operation methods.
    pass


train = CRUDTrain(Train)
