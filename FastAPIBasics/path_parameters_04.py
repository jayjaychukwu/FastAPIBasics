"""
Advanced validation with fastapi Path function
"""
from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/users/{id}/")
async def get_user(id: int = Path(..., ge=1)):  # the three dots ... is called Ellipsis.
    """
    The ellipsis is used to tell FastAPI that we do not want a default value for the parameter
    as the first argument as the parameter is required.
    """
    return {"id": id}
