from fastapi import FastAPI
from core.config import settings
from db.session import engine
from db.base_class import Base

app = FastAPI(title="Blog", version='0.1.0')

@app.get("/")
def home():
    return {"msg": "Hello FastAPI"}
