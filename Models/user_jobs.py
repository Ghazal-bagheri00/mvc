from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base

class UserJobDB(Base):
    __tablename__ = "user_jobs"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, ForeignKey("users.username"))
    job_id = Column(Integer, ForeignKey("jobs.id"))
