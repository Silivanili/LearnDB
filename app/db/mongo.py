import os
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import ReturnDocument
from fastapi import Depends

MONGODB_URL = os.getenv("MONGODB_URL")             
MONGODB_DB = os.getenv("MONGODB_DATABASE")         

client: AsyncIOMotorClient = None
db = None

async def connect_to_mongo():
    global client, db
    client = AsyncIOMotorClient(MONGODB_URL)        
    db = client[MONGODB_DB]

async def close_mongo_connection():
    client.close()

def get_database():
    return db
