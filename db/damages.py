from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from models.Damage import Damage

async def create_damage(db: AsyncSession, side_of_building, floor_of_building, faculty, description, image_link, user_email):
    new_damage = Damage(
        side_of_building=side_of_building,
        floor_of_building=floor_of_building,
        faculty=faculty,
        description=description,
        image_link=image_link,
        user_email=user_email
    )
    db.add(new_damage)
    await db.commit()
    await db.refresh(new_damage)
    return new_damage


async def get_damage(db: AsyncSession, damage_id: int):
    result = await db.execute(select(Damage).where(Damage.id == damage_id))
    return result.scalars().first()


async def get_damages(db: AsyncSession, skip: int = 0, limit: int = 100):
    result = await db.execute(select(Damage).offset(skip).limit(limit))
    return result.scalars().all()


async def update_damage_status(db: AsyncSession, damage_id: int, new_status: str):
    result = await db.execute(select(Damage).where(Damage.id == damage_id))
    damage = result.scalars().first()
    if not damage:
        return None
    damage.status = new_status
    await db.commit()
    await db.refresh(damage)
    return damage


async def delete_damage(db: AsyncSession, damage_id: int):
    result = await db.execute(select(Damage).where(Damage.id == damage_id))
    damage = result.scalars().first()
    if not damage:
        return None
    await db.delete(damage)
    await db.commit()
    return damage