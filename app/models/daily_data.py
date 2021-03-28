from sqlalchemy import Column, Integer, DateTime

from app.database.base_class import Base


class DailyData(Base):
    id = Column(Integer, primary_key=True, index=True)
    train_id = Column(Integer, nullable=False)
    actual_arrival = Column(DateTime, nullable=False)
    actual_departure = Column(DateTime, nullable=False)
