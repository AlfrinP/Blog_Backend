from pydantic import BaseModel
from author.authorDTO import AuthorDto


class BlogCreateRequestDTO(BaseModel):
    title: str
    description: str
    author: AuthorDto
    timeToRead: str
    category: str
    data: str
    img: str
    featured: bool
