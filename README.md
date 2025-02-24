# LearnDB
 Das Ziel des Projekts ist die Entwicklung einer Anwendung, die Lernenden ermöglicht, ihr Wissen in einer NO-SQL Datenbank zu speichern und zu verwalten. Zudem wird eine grundlegende Verwaltung von Kursen ermöglicht. Die Anwendung soll dabei nicht nur passive Speicherung, sondern auch aktives Lernen unterstützen. Dies soll zunächst durch Karteikarten erfolgen. 

**Use Case Beschreibung**
Die folgenden Use Cases sind geplant:
- Dokumentverwaltung: Ein Benutzer legt ein neues Dokument an, fügt es einem Topic und einem Kurs hinzu und sucht später nach diesem Dokument über die Suchfunktion.
- Kurseinstellung: Ein Benutzer erstellt einen neuen Kurs, fügt ihm Topics und Dokumente zu und suchtmithilfe der Suchfunktion nach relevanten Inhalten für den Kurs.
- Karteikarten: Ein Benutzer erstellt Karteikarten basierend auf einem Dokument oder Topic eines Kurses und nutzt diese zum Lernen.
- Suche: Ein Benutzer gibt einen Suchbegriff ein und erhält eine Liste von Dokumenten, die zu diesem Begriff passen.
         

**MSCW-Kriterien**

- **Must Have:**
  - CRUD-Operationen für Dokumente und Topics implementieren.
  - Erstellung, Lesen, Bearbeiten und Löschung von Kursen sowie Zuweisung von Dokumenten und Topics zu Kursen.
  - REST-Schnittstelle für alle Operationen bereitstellen, einschließlich Suchfunktion.
  - Daten in einer NoSQL-Datenbank (MongoDB) speichern.
  - Anwendung containerisieren (Docker).
  - Ausführliche Dokumentation liefern.
  - Code in einem Git-Repository verfügbar machen.
  - Karteikartenfunktion für aktives Lernen umsetzen.

- **Should Have:**
  - Volltextsuche für Dokumente anhand von Titel, Inhalt oder Schlagwörtern implementieren.
  - Logging und grundlegende Fehlerbehandlung integrieren.
  - Rudimentäre Benutzerverwaltung als Platzhalter für spätere Erweiterungen.

     
    
- **Could Have:**
  - Weitere Lernfeatures wie Quizzes hinzufügen. 
  - Speicherung von Fortschritten und Statistiken zu den Kursen und Karteikarten eines Benutzers.

- **Won't Have:**
  - Es wird keine vollwertige Frontend-Benutzeroberfläche entwickelt – der Fokus liegt auf der Backend-Implementierung und der REST-API.


**UML-Klassendiagramm**
Hier ist das momentane Klassendiagramm
![UML-Diagramm](out/Klassendiagramm/Klassendiagramm.png)


**Techstack**
- Backend: FastAPI für die Implementierung der REST-Schnittstelle.
- Datenbank: MongoDB als NoSQL-Datenbank.
- Containerisierung: Docker für die Verwaltung des Services.