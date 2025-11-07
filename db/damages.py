from sqlalchemy import Session
from models.Damage import Damage
from utils.email import send_email


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()


def create_damage(db: Session, side_of_building: str, floor_of_building: int, faculty: str, description: str, image_link: str, user_email: str):
    db_damage = Damage(
        side_of_building=side_of_building,
        floor_of_building=floor_of_building,
        faculty=faculty,
        description=description,
        image_link=image_link,
        user_email=user_email
    )
    db.add(db_damage)
    db.commit()
    db.refresh(db_damage)
    try:
        send_email(
            to_email=user_email,
            subject=f"Damage Report {db_damage.id} Received",
            body=f"A new damage report has been created with ID {db_damage.id}."
        )
    except Exception as e:
        print(f"Error sending email notification: {e}")

    return db_damage

def get_damage(db: Session, damage_id: int):
    return db.query(Damage).filter(Damage.id == damage_id).first()

def get_damages(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Damage).offset(skip).limit(limit).all()

def update_damage_status(db: Session, damage_id: int, new_status: str):
    db_damage = db.query(Damage).filter(Damage.id == damage_id).first()
    if db_damage:
        db_damage.status = new_status
        db.commit()
        db.refresh(db_damage)
    return db_damage

def delete_damage(db: Session, damage_id: int):
    db_damage = db.query(Damage).filter(Damage.id == damage_id).first()
    if db_damage:
        db.delete(db_damage)
        db.commit()
    return db_damage