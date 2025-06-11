from typing import Optional
from fastapi import FastAPI, HTTPException
from enum import Enum

app = FastAPI()

@app.get(
    "/", 
    tags=["Root"], 
    summary="Welcome endpoint", 
    description="This is the root endpoint of the API. It simply returns a greeting message.",
    response_description="A welcome message is returned."
)
def index():
    return {"message": "Hello, FastAPI!"}


@app.get(
    "/blog/all", 
    tags=["Blogs"], 
    summary="Get all blogs", 
    description="Returns a list of all blogs. You can provide pagination parameters such as page number and page size.",
    response_description="A list of blogs with optional pagination."
)
def getAllBlogs(page: int = 1, pageSize: Optional[int] = None):
    return {"message": f'All {pageSize} blogs on page {page}'}


@app.get(
    "/blog/{id}/comments/{commentId}", 
    tags=["Comments"], 
    summary="Get a specific comment on a blog", 
    description="Retrieves a specific comment for a given blog post. You can also filter by `valid` flag and `username`.",
    response_description="Details of the requested comment."
)
def getComment(id: int, commentId: int, valid: bool = True, username: Optional[str] = None):
    return {"message": f'blogId {id}, commentId {commentId}, valid {valid}, username {username}'}


class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'


@app.get(
    '/blog/type/{type}', 
    tags=["Blogs"], 
    summary="Get blogs by type", 
    description="Returns blogs filtered by type. Supported types are: 'short', 'story', and 'howto'.",
    response_description="Returns the selected blog type."
)
def getBlogType(type: BlogType):
    return {'message': f'Blog type {type.value}'}


@app.get(
    "/blog/{id}", 
    tags=["Blogs"], 
    summary="Get a blog by ID", 
    description="Fetch a blog post by its ID. If the ID is greater than 5, a 404 error will be returned.",
    response_description="Blog details if found; otherwise a 404 error."
)
def getBlog(id: int):
    if id > 5:
        raise HTTPException(status_code=404, detail="Not Found")
    return {"message": f"Blog {id}"}
