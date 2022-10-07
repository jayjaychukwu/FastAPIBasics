"""
Get the header from a request
"""
from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/")
async def get_header(hello: str = Header(...)):
    return {"hello": hello}


"""
Get the User-Agent from a request
"""


@app.get("/ua")
async def get_header(user_agent: str = Header(...)):
    return {"user_agent": user_agent}
