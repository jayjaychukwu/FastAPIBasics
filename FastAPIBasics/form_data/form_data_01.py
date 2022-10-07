"""
Using the Form method to accept Form data from
a request
"""

from fastapi import FastAPI, Form

app = FastAPI()


@app.post("/users")
async def create_user(name: str = Form(...), age: int = Form(...)):
    return {"name": name, "age": age}
