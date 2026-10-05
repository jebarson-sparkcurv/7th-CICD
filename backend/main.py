from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Shopping Backend - Version 6"}

@app.get("/health")
def health():
    return {"status": "healthy"}
