# src/blog/blogDAO.py
from pydoc import doc
from typing import List, Optional
from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorDatabase
from .blog import Blog
from .blogDTO import BlogResponseDTO, BlogResponseDTOBuilder


class BlogDAO:
    def __init__(self, db: AsyncIOMotorDatabase):
        self.db = db
        self.collection = db["blogs"]

    async def find_by_id(self, blog_id: str) -> BlogResponseDTO:
        try:
            obj_id = ObjectId(blog_id)
        except Exception:
            return None
        doc = await self.collection.find_one({"_id": obj_id})

        if doc and "_id" in doc:
            doc["blogId"] = str(doc.pop("_id"))  # Map _id to blogId as a string

        print(f"Retrieved blog: {doc}")
        return doc if doc else None

    async def find_all(self) -> List[BlogResponseDTO]:
        cursor = self.collection.find()
        docs = await cursor.to_list(length=6)
        blogList = []
        for doc in docs:
            blogList.append(BlogResponseDTOBuilder(doc))
        return blogList

    async def find_recent(self) -> List[BlogResponseDTO]:
        cursor = self.collection.find().sort("createdAt", -1).limit(6)
        docs = await cursor.to_list(length=6)
        recentBlogList = []
        for doc in docs:
            recentBlogList.append(BlogResponseDTOBuilder(doc))
        return recentBlogList

    async def find_featured(self) -> List[BlogResponseDTO]:
        cursor = self.collection.find({"featured": True})
        docs = await cursor.to_list(length=100)
        featuredBlogList = []
        for doc in docs:
            featuredBlogList.append(BlogResponseDTOBuilder(doc))
        return featuredBlogList

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
