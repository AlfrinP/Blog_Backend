# import fast api
from fastapi import FastAPI

# imports for the MongoDB database connection
from motor.motor_asyncio import AsyncIOMotorClient

# import for fast api lifespan
from contextlib import asynccontextmanager

from dotenv import load_dotenv

config = load_dotenv()


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Start the database connection
    await startup_db_client(app)
    yield
    # Close the database connection
    await shutdown_db_client(app)

# method for start the MongoDb Connection


async def startup_db_client(app):
    app.mongodb_client = AsyncIOMotorClient(
        config.MONGODB_CONNECTION_URI)
    app.mongodb = app.mongodb_client.get_database(config.DB_NAME)
    print("MongoDB connected.")

# method to close the database connection


async def shutdown_db_client(app):
    app.mongodb_client.close()
    print("Database disconnected.")

# creating a server with python FastAPI
db = FastAPI(lifespan=lifespan)
