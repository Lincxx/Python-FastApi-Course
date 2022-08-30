from pickle import FALSE
from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange

app = FastAPI()

# what do we want for a post "schema"
# title str, content str,
class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


my_posts = [
            {"title":"post 1", "content": "content 1", "id": 1},
            {"title":"post 2", "content": "content 2", "id": 2}
            ]

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p

# path operation
@app.get("/")
def root():
    return {"message": "welcome to my api"}

@app.get("/posts")
def get_posts():
    return {"data": my_posts }

@app.post("/posts")
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0,10000000)
    my_posts.append(post_dict)
    return {"data": post_dict}

@app.get("/posts/{id}")
def get_post(id: int):
    post = find_post(id)
    return {"post_details": post}



