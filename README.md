# PDF Bearbeitungstool
## Projektbeschreibung
Ein einfaches PDF-Bearbeitungstool geschrieben in Python. Es ermöglicht das Zusammenfügen und Trennen von PDFs. Dafür wurde die PyPDF2-Bibliothek verwendet. Die Nutzereingaben erfolgen über ein GUI das mit Tkinter umgesetzt wurde.

## Inhaltsverzeichnis
* Projektbeschreibung
* Installation
* Verwendung
* Erkenntnisse

## Installation
Um das Programm auszuführen ist Folgendes nötig:
* Python Interpreter: zur Ausführung des Programms.
* Python File PDF-Bearbeitungstool.py: enthält den Code.
* PyPDF2 Bibliothek: enthält wichtige Funktionen
  * PyPDF2 installieren: In einer Kommandozeile/einem Terminal diesen Befehl ausführen: pip install PyPDF2
* File ausführen

## Verwendung
Um die Verwendung zu erleichtern habe ich ein GUI gestaltet. Dieses leitet selbsterklärend an.

#### Funktionen
* Start: Wenn man das Python-File ausführt öffnet sich das Startfenster. Dieses  beinhaltet zwei Buttons einer für die Funktion "PDFs zusammenfügen" und einen für die Funktion "PDF trennen".
* PDFs zusammenfügen: Mit Klick auf den Button "PDFs Zusammenfügen" öffnet sich ein weiteres Tkinter Fenster.
* Zusammenfügen:
  * Dateien Auswählen: Mit Klick auf den Button "Datei Auswählen" lassen sich via Datei-Explorer-Fenster PDF-Dateien auswählen.  
  Die Ausgewählten Dateien werden auf dem Fenster angezeigt (im Bereich unter "Ausgewählte Dateien:").  
  Achtung: Nur PDF-Dateien möglich.
  * Eingabe zurücksetzen: Hat man einmal eine falsche PDF-Datei ausgewählt, kann man mit Klick auf "Eingabe zurücksetzen" die ausgewählten Files wieder löschen.
  * Neuen Namen für des PDF eingeben: Im unteren Teil des Tkinter Fenster kann man in ein Tkinter-Entry Feld einen Namen für das zusammengefügte PDF eingeben.  
  Gibt man keinen Namen ein heisst das neue PDF einfach ".pdf".  
  Achtung: Name darf keines dieser Zeichen enthalten: \/:*?"<>¦
  * Zurück zum Start: Mit dem Button "Zurück" im rechten oberen Ecken kann man auf den Start zurückkehren.
  * PDF zusammenfügen: Mit Klick auf den Button "Zusammenfügen!" kann man die ausgewählten PDFs zu einem zusammenfügen.  
  Das Zusammengefügen kann einige Sekunden gehen (je nach Anzahl hochgeladener PDFs). Das zusammengefügte PDF wird im selben Ordner wie das Python File gespeichert.  
  Es lassen sich grundsätzlich beliebig viele PDFs zusammenfügen, die benötigte Zeit dafür verlängert sich aber.
  * Hat das Zusammenfügen geklappt öffnet sich ein neues Fenster. Dieses enthält einen Button mit dem man auf den Start zurückkehren kann.
* PDF trennen: Mit Klick auf den Button "PDF trennen" öffnet sich ein weiteres Tkinter Fenster.
* Trennen:
  * Dateien Auswählen: Mit Klick auf den Button "Datei Auswählen" lassen sich via Datei-Explorer-Fenster PDF-Dateien auswählen.  
  Die Ausgewählten Dateien werden auf dem Fenster angezeigt (im Bereich unter "Ausgewählte Dateien:").  
  Achtung: Nur PDF-Dateien möglich.
  * Eingabe zurücksetzen: Hat man einmal eine falsche PDF-Datei ausgewählt, kann man mit Klick auf "Eingabe zurücksetzen" die ausgewählten Files wieder löschen.
  * Zurück zum Start: Mit dem Button "Zurück" im rechten oberen Ecken kann man auf den Start zurückkehren.
  * Seitenbereich eingeben: Im unteren Bereich des Fensters hat es zwei Tkinter-Entry Felder ("Von Seite..." "bis Seite..."). In diese kann man nun den Seitenbereich eingeben.  
  Achtung: Auf Beschriftung achten ("Von Seite..." -> 1. Seite des herausgetrennten PDFs, "bis Seite..." -> letzte Seite des herausgetrennten PDFs).  
  Achtung: Der gewählte Seitenbereich muss möglich sein (innerhalb des PDFs).
  * Neuen Namen für des PDF eingeben: Im unteren Teil des Tkinter Fenster kann man in ein Tkinter-Entry Feld einen Namen für das zusammengefügte PDF eingeben.  
    Gibt man keinen Namen ein heisst das neue PDF einfach ".pdf".  
    Achtung: Name darf keines dieser Zeichen enthalten: \/:*?"<>¦
  * PDF trennen: Mit Klick auf den Button "Trennen!" kann man den ausgewählten Seitenbereich aus dem gewählten PDF heraustrennen.   
    Das Trennen kann einige Sekunden gehen (je nach Grösse des Seitenbereichs). Das getrennte PDF wird im selben Ordner wie das Python File gespeichert.
  * Hat das Trennen geklappt öffnet sich ein neues Fenster. Dieses enthält einen Button mit dem man auf den Start zurückkehren kann.


## Fehlerbehebung
Ich habe probiert den Code so robust wie möglich zu schreiben. Zudem habe ich mir  Zeit genommen das Programm zu testen. 
Sollten trotzdem Abstürze/Fehler auftreten, empfehle ich das Programm zu schliessen und nochmals auszuführen.
Zudem würde ich die Eingabe nochmals überprüfen.
Es kann sein, dass das bearbeitete PDF nicht im gleichen Ordner wie das Python-File gespeichert wird. Das ist eigentlich so nicht vorgesehen und ich konnte auch keine Lösung dazu finden. Kommt das vor kann es sein, dass das File sich im aktuellen Benutzer auf dem C\: ist.


## Quellen
https://pypdf2.readthedocs.io/en/3.0.0/user/installation.html  
https://www.geeksforgeeks.org/python-tkinter-tutorial/  
https://www.youtube.com/watch?v=JKXmp5ZbJ5g  
https://www.youtube.com/watch?v=Aim_7fC-inw  
https://www.python-lernen.de/tkinter-steuerelemente.htm  
https://docs.python.org/3/library/tkinter.html#navigating-the-tcl-tk-reference-manual  
https://www.python-forum.de/  
https://www.delftstack.com/  
https://chatgpt.com/  
https://www.youtube.com/watch?v=ghjfOPk-vs4  
https://www.youtube.com/@BroCodez  
https://docs.kanaries.net/  
https://stackoverflow.com/questions/14900510/changing-the-application-and-taskbar-icon-python-tkinter 

## Autor
Lars Leuenberger
