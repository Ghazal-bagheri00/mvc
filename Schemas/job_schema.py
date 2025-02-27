from pydantic import BaseModel

class Job(BaseModel):
    title: str
    description: str
    city_id: int

class JobOut(Job):
    id: int
