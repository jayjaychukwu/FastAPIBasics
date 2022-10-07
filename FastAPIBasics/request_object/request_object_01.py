"""
Sometimes you might find yourself needing the raw request
object with all the data associated with it. Here is how
you do it
"""
from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/")
async def get_request_object(request: Request):
    return {"path": request.url.path}
