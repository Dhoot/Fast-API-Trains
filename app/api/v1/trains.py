from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import schemas, crud
from app.api.deps import get_db

router = APIRouter()


@router.get("", response_model=List[schemas.TrainResponse])
def read_trains(db: Session = Depends(get_db), skip: int = 0, limit: int = 100) -> Any:
    """
    Retrieve all Trains.
    """
    trains = crud.train.get_multi(db, skip=skip, limit=limit)
    return trains


@router.post("", response_model=schemas.TrainResponse)
def create_train(*, db: Session = Depends(get_db), train_in: schemas.TrainCreate) -> Any:
    """
    Create new train.
    """
    train = crud.train.create(db, obj_in=train_in)
    return train


@router.put("", response_model=schemas.TrainResponse)
def update_train(*, db: Session = Depends(get_db), train_in: schemas.TrainUpdate) -> Any:
    """
    Update existing train.
    """
    train = crud.train.get(db, model_id=train_in.id)
    if not train:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The train with this ID does not exist in the system.",
        )
    train = crud.train.update(db, db_obj=train, obj_in=train_in)
    return train


@router.delete("", response_model=schemas.Message)
def delete_train(*, db: Session = Depends(get_db), id: int) -> Any:
    """
    Delete existing train.
    """
    train = crud.train.get(db, model_id=id)
    if not train:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The train with this ID does not exist in the system.",
        )
    crud.train.remove(db, model_id=train.id)
    return {"message": f"Train with ID = {id} deleted."}
