from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import schemas, crud
from app.api.deps import get_db

router = APIRouter()


@router.get("", response_model=List[schemas.TrainResponse])
def read_daily_datas(db: Session = Depends(get_db), skip: int = 0, limit: int = 100) -> Any:
    """
    Retrieve all Trains.
    """
    daily_datas = crud.daily_data.get_multi(db, skip=skip, limit=limit)
    return daily_datas


@router.post("", response_model=schemas.TrainResponse)
def create_daily_data(*, db: Session = Depends(get_db), daily_data_in: schemas.TrainCreate) -> Any:
    """
    Create new daily_data.
    """
    daily_data = crud.daily_data.create(db, obj_in=daily_data_in)
    return daily_data


@router.put("", response_model=schemas.TrainResponse)
def update_daily_data(*, db: Session = Depends(get_db), daily_data_in: schemas.TrainUpdate) -> Any:
    """
    Update existing daily_data.
    """
    daily_data = crud.daily_data.get(db, model_id=daily_data_in.id)
    if not daily_data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The daily data with this ID does not exist in the system.",
        )
    daily_data = crud.daily_data.update(db, db_obj=daily_data, obj_in=daily_data_in)
    return daily_data


@router.delete("", response_model=schemas.Message)
def delete_daily_data(*, db: Session = Depends(get_db), id: int) -> Any:
    """
    Delete existing daily_data.
    """
    daily_data = crud.daily_data.get(db, model_id=id)
    if not daily_data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The daily data with this ID does not exist in the system.",
        )
    crud.daily_data.remove(db, model_id=daily_data.id)
    return {"message": f"Daily data with ID = {id} deleted."}
