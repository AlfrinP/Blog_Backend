# src/blog/blogController.py
from fastapi import APIRouter, Depends, HTTPException
from typing import List
from motor.motor_asyncio import AsyncIOMotorDatabase

from blog.blogDTO import BlogCreateRequestDTO
from .blog import Blog
from .blogService import BlogService
from dependencies import get_database  # Fix relative import

blog_router = APIRouter(prefix="/blogs", tags=["blogs"])


def get_blog_service(db: AsyncIOMotorDatabase = Depends(get_database)) -> BlogService:
    return BlogService(db)


@blog_router.get("/", response_model=List[Blog])
async def list_blogs(service: BlogService = Depends(get_blog_service)):
    return await service.get_all()


@blog_router.get("/recent", response_model=List[Blog])
async def recent_blogs(service: BlogService = Depends(get_blog_service)):
    return await service.get_recent()


@blog_router.get("/featured", response_model=List[Blog])
async def featured_blogs(service: BlogService = Depends(get_blog_service)):
    return await service.get_featured()


@blog_router.get("/{blog_id}", response_model=Blog)
async def get_blog(
    blog_id: str,
    service: BlogService = Depends(get_blog_service)
):
    blog = await service.get_by_id(blog_id)
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    return blog


@blog_router.post("/", response_model=str)
async def create_blog(
    blog: BlogCreateRequestDTO,
    service: BlogService = Depends(get_blog_service)
):
    return await service.create(blog.model_dump())


@blog_router.put("/{blog_id}", response_model=int)
async def update_blog(
    blog_id: str,
    update_data: dict,
    service: BlogService = Depends(get_blog_service)
):
    return await service.update(blog_id, update_data)


@blog_router.delete("/{blog_id}", response_model=int)
async def delete_blog(
    blog_id: str,
    service: BlogService = Depends(get_blog_service)
):
    return await service.delete(blog_id)
