from fastapi import FastAPI

app = FastAPI(title="Production FastAPI API", version="1.0.0")


@app.get("/healths")
def health_check():
    return {"status": "healthy"}
