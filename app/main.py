from fastapi import FastAPI
from api.endpoints import dokument, autor, karteikarte, benutzer, kurs, topic
from db.mongo import connect_to_mongo, close_mongo_connection

app = FastAPI(title="LearnDB API", debug=True)

@app.on_event("startup")
async def startup_db_client():
    await connect_to_mongo()                      

@app.on_event("shutdown")
async def shutdown_db_client():
    await close_mongo_connection()

app.include_router(dokument.router, prefix="/api/dokument", tags=["Dokument"])
app.include_router(autor.router, prefix="/api/autor", tags=["Autor"])
app.include_router(karteikarte.router, prefix="/api/karteikarte", tags=["Karteikarte"])
app.include_router(benutzer.router, prefix="/api/benutzer", tags=["Benutzer"])
app.include_router(kurs.router, prefix="/api/kurs", tags=["Kurs"])
app.include_router(topic.router, prefix="/api/topic", tags=["Topic"])

@app.get("/")
def read_root():
    return {"message": "Willkommen zur LearnDB API"}
