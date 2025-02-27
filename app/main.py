from fastapi import FastAPI
from app.Views import user_view, job_view, city_view




app = FastAPI()

app.include_router(user_view.router, prefix="/v1")
app.include_router(job_view.router, prefix="/v1")
app.include_router(city_view.router, prefix="/v1")

@app.get("/")
def home():
    return {"message": "Welcome to the Job API"}
