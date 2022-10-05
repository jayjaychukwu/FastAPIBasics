from enum import Enum

from fastapi import FastAPI, Query

app = FastAPI()


class UsersFormat(str, Enum):
    SHORT = "short"
    FULL = "full"


"""
You can leave this without any query because the queries have a default value
"""


@app.get("/users")
async def get_user(page: int = 1, size: int = 10):
    return {"page": page, "size": size}


"""
This will return a 422 Unprocessable Entity because no format was part of the query
"""


@app.get("/usersf")
async def get_userf(format: UsersFormat):
    return {"format": format}


"""
The page must be greater than 0 and the size must be less than
or equal to 100
"""


@app.get("/usersq")
async def get_userq(page: int = Query(1, gt=0), size: int = Query(10, le=100)):
    return {"page": page, "size": size}
