from pydantic import BaseModel


class AuthorDto(BaseModel):
    profilePic: str
    authorName: str
