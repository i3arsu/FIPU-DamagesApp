from sqlalchemy import Column, Integer, String
from database import Base

class Damage(Base):
    __tablename__ = "damages"

    id = Column(Integer, primary_key=True, index=True)
    side_of_building = Column(String, nullable=False)
    floor_of_building = Column(Integer, nullable=False)
    faculty = Column(String, nullable=False)
    status = Column(String, default="Reported", nullable=False)
    description = Column(String, unique=True, nullable=False)
    image_link = Column(String, unique=True, index=True, nullable=True)
    user_email = Column(String, unique=True, index=True, nullable=False)