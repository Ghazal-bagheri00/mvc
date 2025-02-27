from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.Schemas.city_schema import City, CityOut
from app.Controllers.city_controller import create_city, get_cities
from app.database import get_db

router = APIRouter()

@router.post("/cities", response_model=CityOut)
def add_city(city: City, db: Session = Depends(get_db)):
    return create_city(db, city.name)

@router.get("/cities", response_model=list[CityOut])
def list_cities(db: Session = Depends(get_db)):
    return get_cities(db)
