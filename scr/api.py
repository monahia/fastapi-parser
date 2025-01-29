from fastapi import FastAPI
from data import DataBase


app = FastAPI()
db = DataBase("database.db")

@app.get("/users/{user_name}")
async def get_item(user_name: str | None = None):
    return db.getUserByName(user_name)
    
@app.get("/")
async def root():
    return "hello user!"