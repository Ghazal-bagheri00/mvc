from pydantic import BaseModel

class City(BaseModel):
    name: str

class CityOut(City):
    id: int

