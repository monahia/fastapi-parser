from fastapi import FastAPI  # import api

from data import DataBase  # local database script


app = FastAPI()
db = DataBase("database.db")


@app.get("/users/{user_name}")  # route for get users by name
async def get_item(user_name: str):
    result = db.getUserByName(user_name)
    if result:
        return result
    return "User not found, select another user", db.getAllNames()
        
    
@app.get("/")  # route for root
async def root():
    return "hello user!"