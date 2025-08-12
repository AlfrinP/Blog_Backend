from pydantic import BaseModel
from src.author.authorDTO import AuthorDto
from src.blog.blog import Blog

class BlogCreateRequestDTO(BaseModel):
    title: str
    description: str
    author: AuthorDto
    timeToRead: str
    category: str
    data: str
    img: str
    featured: bool


class BlogResponseDTO(BaseModel):
    blogId: str
    title: str
    description: str
    author: AuthorDto
    timeToRead: str
    category: str
    data: str
    img: str
    featured: bool

def BlogResponseDTOBuilder(blog: dict) -> BlogResponseDTO:
    if "_id" in blog:
        blog["blogId"] = str(blog.pop("_id"))
    return BlogResponseDTO(**blog)
