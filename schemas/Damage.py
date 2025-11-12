# schemas/damage_schema.py
from pydantic import BaseModel
from typing import Optional

class DamageBase(BaseModel):
    side_of_building: str
    floor_of_building: int
    faculty: str
    status: str
    description: str
    image_link: Optional[str] = None
    user_email: str

class DamageCreate(DamageBase):
    pass

class DamageResponse(DamageBase):
    id: int
    class Config:
        from_attributes = True  # Pydantic v2