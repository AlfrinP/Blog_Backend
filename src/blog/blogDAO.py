# src/blog/blogDAO.py
from typing import List, Optional
from motor.motor_asyncio import AsyncIOMotorDatabase
from .blog import Blog


class BlogDAO:
    def __init__(self, db: AsyncIOMotorDatabase):
        self.db = db
        self.collection = db["blogs"]

    async def find_by_id(self, blog_id: str) -> Optional[Blog]:
        return await self.collection.find_one({"blogId": blog_id})

    async def find_all(self) -> List[Blog]:
        cursor = self.collection.find()
        return await cursor.to_list(length=100)

    async def find_recent(self) -> List[Blog]:
        cursor = self.collection.find().sort("createdAt", -1).limit(6)
        return await cursor.to_list(length=6)

    async def find_featured(self) -> List[Blog]:
        cursor = self.collection.find({"featured": True})
        return await cursor.to_list(length=100)

    async def insert(self, blog: dict) -> str:
        result = await self.collection.insert_one(blog)
        return str(result.inserted_id)

    async def update(self, blog_id: str, update_data: dict) -> int:
        result = await self.collection.update_one(
            {"blogId": blog_id},
            {"$set": update_data}
        )
        return result.modified_count

    async def delete(self, blog_id: str) -> int:
        result = await self.collection.delete_one({"blogId": blog_id})
        return result.deleted_count
