from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.damages import get_db, create_damage, get_damage, get_damages, update_damage_status, delete_damage
from models.Damage import Damage

router = APIRouter(
    prefix="/damages",
    tags=["damages"])

@router.post("/", response_model=Damage)
async def report_damage(side_of_building: str, 
                        floor_of_building: int, 
                        faculty: str, 
                        description: str, 
                        image_link: str, 
                        user_email: str, 
                        db: Session = Depends(get_db)):
    return await create_damage(db, side_of_building, floor_of_building, faculty, description, image_link, user_email)

@router.get("/{damage_id}", response_model=Damage)
async def read_damage(damage_id: int, db: Session = Depends(get_db)):
    db_damage = await get_damage(db, damage_id)
    if db_damage is None:
        raise HTTPException(status_code=404, detail="Damage not found")
    return db_damage

@router.get("/", response_model=list[Damage])
async def read_damages(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return await get_damages(db, skip=skip, limit=limit)

@router.put("/{damage_id}/status", response_model=Damage)
async def change_damage_status(damage_id: int, new_status: str, db: Session = Depends(get_db)):
    db_damage = await update_damage_status(db, damage_id, new_status)
    if db_damage is None:
        raise HTTPException(status_code=404, detail="Damage not found")
    return db_damage

@router.delete("/{damage_id}", response_model=Damage)
async def remove_damage(damage_id: int, db: Session = Depends(get_db)):
    db_damage = await delete_damage(db, damage_id)
    if db_damage is None:
        raise HTTPException(status_code=404, detail="Damage not found")
    return db_damage