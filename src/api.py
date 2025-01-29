from fastapi import FastAPI
from data import DataBase


app = FastAPI()
db = DataBase("database.db")

@app.get("/users/{user_name}")
async def get_item(user_name: str):
    result = db.getUserByName(user_name)
    if result:
        return result
    return [
        "User not found, select another user",
        db.getAllUsers()
        ]
    
@app.get("/")
async def root():
    return "hello user!"