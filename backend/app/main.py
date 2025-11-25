from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/health", status_code=200)
def health_check():
    today = datetime.now()
    return {
        "status": "ok",
        "date": today.strftime("%Y-%m-%d-%H:%M:%S")
    }