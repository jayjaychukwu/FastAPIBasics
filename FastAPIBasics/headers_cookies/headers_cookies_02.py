"""
Obtaining a cookie from the request,
where the cookie Optional,
and the default value of the cookie is None
"""
from typing import Optional

from fastapi import Cookie, FastAPI

app = FastAPI()


@app.get("/")
async def get_cookie(hello: Optional[str] = Cookie(None)):
    return {"hello": hello}
