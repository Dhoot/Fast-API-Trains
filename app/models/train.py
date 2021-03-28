from sqlalchemy import Column, Integer, String, Time

from app.database.base_class import Base


class Train(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    expected_arrival_time = Column(Time, nullable=False)
    expected_departure_time = Column(Time, nullable=False)
