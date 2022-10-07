"""
How to use pydantic models for data validation
"""
from fastapi import FastAPI
from pydantic import BaseModel


class User(BaseModel):
    name: str
    age: int


app = FastAPI()


@app.post("/users")
async def create_user(user: User):
    return user


"""
Assuming you wish to pass multiple objects in the request
"""


class Company(BaseModel):
    name: str


@app.post("/userscom")
async def create_usercom(user: User, company: Company):
    return {"user": user, "company": company}
