from fastapi import FastAPI
import model
from config import engine

model.Base.metadata.create_all(bind=engine)


app = FastAPI()


@app.get('/')
async def home():
    return "Welcome Home"

