# src/dependencies.py
from fastapi import Request
from motor.motor_asyncio import AsyncIOMotorDatabase


async def get_database(request: Request) -> AsyncIOMotorDatabase:
    if not hasattr(request.app.state, "mongodb"):
        raise RuntimeError(
            "MongoDB client not initialized. "
            "Make sure your FastAPI app is using the correct lifespan."
        )
    return request.app.state.mongodb
