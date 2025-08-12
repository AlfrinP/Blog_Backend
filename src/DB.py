# import fast api
import os
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from contextlib import asynccontextmanager
from dotenv import load_dotenv


load_dotenv()


MONGODB_CONNECTION_URI = os.getenv("MONGODB_CONNECTION_URI")
DB_NAME = os.getenv("DB_NAME")

# Check if required environment variables are set
if not MONGODB_CONNECTION_URI:
    raise ValueError(
        "MONGODB_CONNECTION_URI environment variable is not set. Please check your .env file.")

if not DB_NAME:
    raise ValueError(
        "DB_NAME environment variable is not set. Please check your .env file.")


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Start the database connection
    await startup_db_client(app)
    yield
    # Close the database connection
    await shutdown_db_client(app)

# method for start the MongoDb Connection


async def startup_db_client(app):
    try:
        app.state.mongodb_client = AsyncIOMotorClient(MONGODB_CONNECTION_URI)
        app.state.mongodb = app.state.mongodb_client.get_database(DB_NAME)
        # Test the connection
        await app.state.mongodb.list_collection_names()
        print("MongoDB connected successfully.")
    except Exception as e:
        print(f"Failed to connect to MongoDB: {e}")
        raise e

# method to close the database connection


async def shutdown_db_client(app):
    app.state.mongodb_client.close()
    print("Database disconnected.")
