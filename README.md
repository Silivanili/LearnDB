# LearnDB
 Dieses Semesterprojekt soll Lernenden helfen, ihr Wissen in einer Datenbankstruktur zu speichern und zu verwalten. Aktives Lernen soll auch möglich sein, zunächst in Form von Karteikarten.



**Use Case Beschreibung**
  
Die Anwendung soll es dem Benutzer ermöglichen, Dokumente (z. B. Vorlesungsunterlagen, Skripte, Übungsblätter) und Topics anzulegen, zu bearbeiten, abzurufen und zu löschen. Zusätzlich soll eine einfache Suchfunktion integriert werden, um relevante Dokumente anhand von Metadaten (z. B. Titel, Schlagwörter) schnell zu finden. Der Benutzer soll aktiv lernen können, etwa durch Karteikarten. Um das Projekt agil zu halten werden die Anforderungen in MSCW-Kriterien unterteilt.

**MSCW-Kriterien**

- **Must Have:**
  - Die Anwendung muss CRUD-Operationen für Dokumente unterstützen (Erstellen, Lesen, Aktualisieren, Löschen).
  - Es muss eine REST-Schnittstelle implementiert werden, die alle CRUD-Operationen sowie eine einfache Suchfunktion bereitstellt.
  - Die Dokumentdaten müssen in einer NO-SQL-Datenbank gespeichert werden.
  - Der gesamte Service muss containerisiert sein und verwaltet werden.
  - Eine ausführliche Dokumentation muss bereitgestellt werden.
  - Der Code muss in einem Git-Repository sein um ihn klonen zu können.


- **Should Have:**
  - Die Anwendung soll eine Volltextsuche ermöglichen, sodass Nutzer Dokumente anhand von Titel, Inhalt oder Schlagwörtern filtern können.
  - Logging und einfache Fehlerbehandlung soll integriert sein, um eine bessere Wartbarkeit zu gewährleisten.
  - Die Anwendung soll dem Benutzer das aktive Lernen durch Karteikarten ermöglichen.
    
- **Could Have:**
  - Eine rudimentäre Benutzerverwaltung (nur als Platzhalter für spätere Erweiterungen) kann integriert werden.
  - Weitere Möglichkeiten dem Benutzer aktiv beim lernen zu helfen, etwa Quizzes.

- **Won't Have:**
  - Es wird keine vollwertige Frontend-Benutzeroberfläche entwickelt – der Fokus liegt auf der Backend-Implementierung und der REST-API.


**UML-Klassendiagramm**
Hier ist das momentane Klassendiagramm
![UML-Diagramm](out/Klassendiagramm/Klassendiagramm.png)


**Techstack**
- FastAPI
- MongoDB
- Docker
