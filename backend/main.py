from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Shopping Backend - Version 1"}

@app.get("/health")
def health():
    raise HTTPException(
        status_code=500,
        detail="V4 intentional health check failure"
    )
