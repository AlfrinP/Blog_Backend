from uuid import UUID, uuid4
from author.author import Author
from pydantic import BaseModel, Field
from datetime import datetime


class Blog(BaseModel):
    blogId: UUID = Field(default_factory=uuid4)
    title: str
    description: str
    author: Author
    timeToRead: str
    category: str
    data: str
    img: str
    createdAt: datetime = Field(default_factory=datetime.utcnow)
    featured: bool
