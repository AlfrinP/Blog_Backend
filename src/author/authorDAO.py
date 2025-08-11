from Db import db
from typing import List, Dict, Optional
from author.author import Author


async def getAuthorById(authorId: str) -> Optional[Author]:
    return await db.mongodb["authors"].find_one({"authorId": authorId})


async def getAuthors() -> List[Author]:
    cursor = db.mongodb["authors"].find()
    return await cursor.to_list(length=100)


async def createAuthor(author: Author) -> str:
    result = await db.mongodb["authors"].insert_one(author)
    return str(result.inserted_id)


async def updateAuthor(authorId: str, updateData: Author) -> int:
    result = await db.mongodb["authors"].update_one({"authorId": authorId}, {"$set": updateData})
    return result.modified_count


async def deleteAuthor(authorId: str) -> int:
    result = await db.mongodb["authors"].delete_one({"authorId": authorId})
    return result.deleted_count
