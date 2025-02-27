from sqlalchemy.orm import Session
from app.Models.jobs import JobDB

def create_job(db: Session, title: str, description: str, city_id: int):
    job = JobDB(title=title, description=description, city_id=city_id)
    db.add(job)
    db.commit()
    return job

def get_jobs(db: Session):
    return db.query(JobDB).all()
