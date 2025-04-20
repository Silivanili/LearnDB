import os
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import ReturnDocument
from fastapi import Depends

MONGODB_URL = os.getenv("MONGODB_URL")      #Hol dir MongoDB-URL und Datenbankname aus dem .env file             
MONGODB_DB = os.getenv("MONGODB_DATABASE")         

client: AsyncIOMotorClient = None
db = None

async def connect_to_mongo():   #Verbinde mit MongoDB mit URL aus dem .env file.
    global client, db
    client = AsyncIOMotorClient(MONGODB_URL)        
    db = client[MONGODB_DB]

async def ensure_text_indexes():    #Erstelle Textindex für die Dokumente, für Textsuche.
    await db.documents.create_index(
        [
            ("titel", "text"),
            ("beschreibung", "text"),
            ("inhalt", "text"),
            ("schlagworte", "text"),
        ],
        default_language="german"
    )
    

async def close_mongo_connection():
    client.close()

def get_database(): #Dadurch können die endpoints auf die Datenbank zugreifen, ohne selbst eine Verbindung herstellen zu müssen.
    return db
