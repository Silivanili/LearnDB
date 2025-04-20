from pymongo import MongoClient
from datetime import datetime
from bson.objectid import ObjectId

client = MongoClient("mongodb://localhost:27017/")
db = client["learn_db"]

# Clear existing collections
db.benutzer.delete_many({})
db.autoren.delete_many({})
db.dokumente.delete_many({})
db.karteikarten.delete_many({})
db.kurse.delete_many({})
db.topics.delete_many({})

# Benutzer
benutzer = [
    {"name": "Anna Muster", "email": "anna@example.com"},
    {"name": "Tom Beispiel", "email": "tom@example.com"}
]
benutzer_ids = db.benutzer.insert_many(benutzer).inserted_ids

# Autoren
autoren = [
    {"name": "Dr. Knowledge", "email": "knowledge@edu.com"},
    {"name": "Prof. Learnwell", "email": "learnwell@edu.com"}
]
autoren_ids = db.autoren.insert_many(autoren).inserted_ids

# Topics
topics = [
    {"name": "Datenbanken", "beschreibung": "Grundlagen von NoSQL und relationalen Datenbanken"},
    {"name": "Programmieren", "beschreibung": "Einführung in Python und JavaScript"}
]
topic_ids = db.topics.insert_many(topics).inserted_ids

# Kurse
kurse = [
    {
        "name": "NoSQL für Einsteiger",
        "beschreibung": "Ein Kurs über dokumentbasierte Datenbanken",
        "ort": "Online",
        "Zeit": datetime(2025, 5, 1, 10, 0),
        "sonstige_infos": "Kursmaterialien inklusive",
        "topics": [topic_ids[0]]
    },
    {
        "name": "Python Basics",
        "beschreibung": "Grundlagen der Python-Programmierung",
        "ort": "Hörsaal 3",
        "Zeit": datetime(2025, 5, 15, 9, 0),
        "sonstige_infos": "Bitte Laptop mitbringen",
        "topics": [topic_ids[1]]
    }
]
kurs_ids = db.kurse.insert_many(kurse).inserted_ids

# Dokumente
dokumente = [
    {
        "titel": "Einführung in MongoDB",
        "beschreibung": "Basics zu MongoDB",
        "inhalt": "MongoDB ist eine dokumentbasierte Datenbank...",
        "erstellungsdatum": datetime.now(),
        "schlagworte": ["MongoDB", "NoSQL", "Database"],
        "kurs": str(kurs_ids[0]),
        "autor_id": str(autoren_ids[0]),
        "topics": [str(topic_ids[0])]
    },
    {
        "titel": "Python Datentypen",
        "beschreibung": "Übersicht über Python-Datentypen",
        "inhalt": "In Python gibt es Strings, Listen, Dictionaries...",
        "erstellungsdatum": datetime.now(),
        "schlagworte": ["Python", "Daten", "Grundlagen"],
        "kurs": str(kurs_ids[1]),
        "autor_id": str(autoren_ids[1]),
        "topics": [str(topic_ids[1])]
    }
]
dokumente_ids = db.dokumente.insert_many(dokumente).inserted_ids

# Karteikarten
karteikarten = [
    {
        "frage": "Was ist MongoDB?",
        "antwort": "Eine dokumentbasierte NoSQL-Datenbank",
        "erstellungsdatum": datetime.now(),
        "kategorie": "Datenbanken",
        "benutzer_id": str(benutzer_ids[0]),
        "dokument_id": str(dokumente_ids[0]),
        "topic_id": str(topic_ids[0]),
        "kurs_id": str(kurs_ids[0])
    },
    {
        "frage": "Was ist ein Dictionary in Python?",
        "antwort": "Ein Key-Value-basiertes Datenstruktur",
        "erstellungsdatum": datetime.now(),
        "kategorie": "Programmieren",
        "benutzer_id": str(benutzer_ids[1]),
        "dokument_id": str(dokumente_ids[1]),
        "topic_id": str(topic_ids[1]),
        "kurs_id": str(kurs_ids[1])
    }
]
db.karteikarten.insert_many(karteikarten)

print("✅ Sample data inserted successfully.")
