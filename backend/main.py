from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Shopping Backend - Version 1"}

@app.get("/health")
def health():
    return {"status": "unhealthy"}, 500
