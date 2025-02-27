from sqlalchemy.orm import Session
from app.Models.cities import CityDB

def create_city(db: Session, name: str):
    city = CityDB(name=name)
    db.add(city)
    db.commit()
    return city

def get_cities(db: Session):
    return db.query(CityDB).all()
