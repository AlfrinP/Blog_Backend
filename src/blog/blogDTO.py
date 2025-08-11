from pydantic import BaseModel


class BlogDTO(BaseModel):
    title: str
    description: str
    author: AuthorDTO
    timeToRead: str
    category: str
    data: str
    img: str
    featured: bool
    createdAt: bool
