from typing import List
from blog.blog import Blog
from Db import db


async def getBlogById(blogId: str):
    return await db.mongodb["blogs"].find_one({"blogId": blogId})


async def getBlogs() -> List[Blog]:
    cursor = db.mongodb["blogs"].find()
    return await cursor.to_list(length=100)


async def getRecentBlogs() -> List[Blog]:
    cursor = db.mongodb["blogs"].find().sort("createdAt", -1).limit(6)
    return await cursor.to_list(length=6)


async def getFeaturedBlogs() -> List[Blog]:
    cursor = db.mongodb["blogs"].find({"featured": True})
    return await cursor.to_list(length=100)


async def createBlogs(blogs: dict):
    result = await db.mongodb["blogs"].insert(blogs)
    return str(result.inserted_id)


async def createBlog(blog: dict):
    result = await db.mongodb["blogs"].insert_one(blog)
    return str(result.inserted_id)


async def updateBlog(blogId: str, updateData: dict):
    result = await db.mongodb["blogs"].update_one({"blogId": blogId}, {"$set": updateData})
    return result.modified_count


async def deleteBlog(blogId: str):
    result = await db.mongodb["blogs"].delete_one({"blogId": blogId})
    return result.deleted_count
