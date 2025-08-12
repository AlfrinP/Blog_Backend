# src/blog/blogService.py
from typing import List, Optional
from motor.motor_asyncio import AsyncIOMotorDatabase
from .blog import Blog
from .blogDAO import BlogDAO


class BlogService:
    def __init__(self, db: AsyncIOMotorDatabase):
        self.dao = BlogDAO(db)

    async def get_by_id(self, blog_id: str) -> Optional[Blog]:
        return await self.dao.find_by_id(blog_id)

    async def get_all(self) -> List[Blog]:
        return await self.dao.find_all()

    async def get_recent(self) -> List[Blog]:
        return await self.dao.find_recent()

    async def get_featured(self) -> List[Blog]:
        return await self.dao.find_featured()

    async def create(self, blog: dict) -> str:
        return await self.dao.insert(blog)

    async def update(self, blog_id: str, update_data: dict) -> int:
        # Here you can add business logic before update
        # For example, validation, timestamps, etc.
        return await self.dao.update(blog_id, update_data)

    async def delete(self, blog_id: str) -> int:
        # Here you can add business logic before deletion
        # For example, check permissions, cascade delete, etc.
        return await self.dao.delete(blog_id)
