from typing import List, Dict, Optional
from .authorDAO import AuthorDAO
from .author import Author
from motor.motor_asyncio import AsyncIOMotorDatabase


class AuthorService:
    def __init__(self, db: AsyncIOMotorDatabase):
        self.dao = AuthorDAO(db)

    async def get_by_id(self, author_id: str) -> Optional[Author]:
        return await self.dao.find_by_id(author_id)

    async def get_all(self) -> List[Author]:
        return await self.dao.find_all()

    async def create(self, author: Author) -> str:
        return await self.dao.insert(author)

    async def update(self, author_id: str, update_data: Dict) -> int:
        return await self.dao.update(author_id, update_data)

    async def delete(self, author_id: str) -> int:
        return await self.dao.delete(author_id)
