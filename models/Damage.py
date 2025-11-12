from sqlalchemy import Column, Integer, String
from db.database import Base

class Damage(Base):
    __tablename__ = "damages"

    id: int = Column(Integer, primary_key=True, index=True)
    side_of_building: str = Column(String, nullable=False)
    floor_of_building: int = Column(Integer, nullable=False)
    faculty: str = Column(String, nullable=False)
    status: str = Column(String, default="Reported", nullable=False)
    description: str = Column(String, unique=True, nullable=False)
    image_link: str | None = Column(String, unique=True, index=True, nullable=True)
    user_email: str = Column(String, unique=True, index=True, nullable=False)