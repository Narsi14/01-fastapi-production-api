from fastapi import FastAPI

from app.api.v1.tasks import router as tasks_router

app = FastAPI(title="Production FastAPI API", version="0.1.0")

app.include_router(tasks_router, prefix="/api/v1")


@app.get("/healths")
def health_check():
    return {"status": "healthy"}
