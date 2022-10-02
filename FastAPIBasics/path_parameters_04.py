"""
Advanced validation with fastapi Path function
"""
from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/users/{id}/")
async def get_user(id: int = Path(..., ge=1)):  # the three dots ... is called Ellipsis
    return {"id": id}
