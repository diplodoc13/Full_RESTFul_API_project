from typing import Optional
from fastapi import Body, FastAPI
from pydantic import BaseModel


app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/posts")
async def get_posts():
    return {"data": "This is your posts"}


@app.post("/createposts")
async def create_posts(post: Post):
    print(post)
    print(post.dict())
    return {"data": post}

