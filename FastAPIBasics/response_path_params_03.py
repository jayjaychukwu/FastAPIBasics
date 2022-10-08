"""
You have a Post Model with several properties like
title and nb_views 
"""
from fastapi import FastAPI
from pydantic import BaseModel


class Post(BaseModel):
    title: str
    nb_views: int


app = FastAPI()

# Dummy database
posts = {
    1: Post(title="Hello", nb_views=100),
}


@app.get("/posts/{id}")
async def get_post(id: int):
    return posts[id]


# The above code returns title and nb_views
# But you want only the tile to show, so what do you do?
# That is what the "response_model" does, look below


class PublicPost(BaseModel):
    title: str


@app.get("/postsr/{id}", response_model=PublicPost)
async def get_post(id: int):
    return posts[id]
