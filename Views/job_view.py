from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.Schemas.job_schema import Job, JobOut
from app.Controllers.job_controller import create_job, get_jobs
from app.database import get_db

router = APIRouter()

@router.post("/jobs", response_model=JobOut)
def add_job(job: Job, db: Session = Depends(get_db)):
    return create_job(db, job.title, job.description, job.city_id)

@router.get("/jobs", response_model=list[JobOut])
def list_jobs(db: Session = Depends(get_db)):
    return get_jobs(db)
