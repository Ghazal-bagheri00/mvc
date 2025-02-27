from sqlalchemy import Column, String, Boolean
from app.database import Base

class UserDB(Base):
    __tablename__ = "users"
    username = Column(String, primary_key=True, index=True)
    password = Column(String)
    is_admin = Column(Boolean, default=False)
