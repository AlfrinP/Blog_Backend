from typing import List, Dict, Optional
from .author import Author


class AuthorDAO:
    def __init__(self):
        self.collection = db.mongodb["authors"]

    async def find_by_id(self, author_id: str) -> Optional[Author]:
        return await self.collection.find_one({"authorId": author_id})

    async def find_all(self) -> List[Author]:
        cursor = self.collection.find()
        return await cursor.to_list(length=100)

    async def insert(self, author: Author) -> str:
        result = await self.collection.insert_one(author.model_dump())
        return str(result.inserted_id)

    async def update(self, author_id: str, update_data: Dict) -> int:
        result = await self.collection.update_one(
            {"authorId": author_id},
            {"$set": update_data}
        )
        return result.modified_count

    async def delete(self, author_id: str) -> int:
        result = await self.collection.delete_one({"authorId": author_id})
        return result.deleted_count
