
from fastapi import APIRouter, HTTPException
from typing import List
from blog.blog import Blog
from blog.blogDAO import (
    getBlogById, getBlogs, getRecentBlogs, getFeaturedBlogs,
    createBlog, updateBlog, deleteBlog
)

router = APIRouter(prefix="/blogs", tags=["blogs"])


@router.get("/", response_model=List[Blog])
async def list_blogs():
    return await getBlogs()


@router.get("/recent", response_model=List[Blog])
async def recent_blogs():
    return await getRecentBlogs()


@router.get("/featured", response_model=List[Blog])
async def featured_blogs():
    return await getFeaturedBlogs()


@router.get("/{blogId}", response_model=Blog)
async def get_blog(blogId: str):
    blog = await getBlogById(blogId)
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    return blog


@router.post("/", response_model=str)
async def create_blog(blog: Blog):
    return await createBlog(blog.dict())


@router.put("/{blogId}", response_model=int)
async def update_blog(blogId: str, updateData: dict):
    return await updateBlog(blogId, updateData)


@router.delete("/{blogId}", response_model=int)
async def delete_blog(blogId: str):
    return await deleteBlog(blogId)
