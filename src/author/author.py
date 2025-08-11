from pydantic import BaseModel
from uuid import UUID, uuid4
from pydantic import BaseModel, Field
from datetime import datetime


class Author(BaseModel):
    authorId: UUID = Field(default_factory=uuid4)
    profilePic: str
    authorName: str
    createdAt: datetime = Field(default_factory=datetime.utcnow)
