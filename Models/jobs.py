from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base

class JobDB(Base):
    __tablename__ = "jobs"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    city_id = Column(Integer, ForeignKey("cities.id"))

