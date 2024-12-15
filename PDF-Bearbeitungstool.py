"""Imports"""
import tkinter as tk
from tkinter import filedialog as fd
import os
from PyPDF2 import PdfWriter, PdfReader
from time import sleep


"""Funktionen"""
#Funktion die das Icon anzeigt
def icon_show(window_name):
    currentRegister = __file__
    addBackslash = currentRegister.replace("\\", "\\\\")
    iconPath = addBackslash.replace("\\PDF-Bearbeitungstool.py", "\\icon.ico")

    window_name.iconbitmap(iconPath)

#Funktion die den Button (Trennen/Zusammenfügen) aktiviert oder deaktiviert je nachdem ob genügend PDFs hochgeladen wurden.
def button_activate(list, name_button, case, name_button2=""):
    if case == 1:
        if len(list) >= 2:
            name_button.config(state="normal") #Button zusammenfügen
        else:
            name_button.config(state="disabled") #Button zusammenfügen
    elif case == 2:
        if len(list) == 1:
            name_button.config(state="normal") #Button trennen
            name_button2.config(state="disabled") #Button Datei auswählen
        else:
            name_button.config(state="disabled") #Button trennen
            name_button2.config(state="normal") #Button Datei auswählen


# Funktion die Filedialog öffnet und so Pfad holt
filenames = []
def chooseFiles(window_name, label_name, button_name, case, button_name2 = ""):
    openExplorer = fd.askopenfilename(initialdir="/", title="Datei Auswählen", filetypes=(("PDF-Dateien", "*.pdf"), ("PDF-Dateien", "*.pdf")))
    path = os.path.realpath(openExplorer) 
    baseFilename = os.path.basename(openExplorer)

    addBackslash = path.replace("\\","\\\\")
    filenames.append(addBackslash)

    window_name.lift() #Fenster in den Vordergrund

    # Text auf Textfeld "label_fileNames" aktualisieren
    currentText = label_name.cget("text")
    newText = currentText + baseFilename + "\n"
    label_name.config(text=newText)
    button_activate(filenames, button_name, case, button_name2)

#Funktion die hochgeladene Dateien löscht
def deleteFiles(label_name, button_name, case, button_name2 = ""):
    filenames.clear() 
    label_name.config(text="")
    button_activate(filenames, button_name, case, button_name2)

#Funktion "Zurück" zerstört den aktuellen Screen -> Start Screen wird angezeigt
def back(window_name):
    window_name.destroy()

#Funktion die nach dem Trennen/Zusammenfügen erscheint
def functionFinished(text):
    """Fenster erstellen"""
    completedScreen = tk.Tk()
    completedScreen.geometry('750x500')
    completedScreen.resizable(False, False)
    completedScreen.configure(background='#f6f6f6')
    completedScreen.title(text)


    """Labels"""
    #Titel "PDF wurde erfolgreich zusammengefügt!"
    label_title = tk.Label(completedScreen, text=text, font=("Nunito Sans", 20, "bold"), fg="#1d1d1d",bg='#f6f6f6')
    label_title.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

    #Weitere Aktionen
    label_instruction = tk.Label(completedScreen, text="Weitere PDFs bearbeiten:", font=("Nunito Sans", 13, "bold"),fg="#1d1d1d", bg='#f6f6f6')
    label_instruction.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

    """Buttons"""
    #Button zurück zum Start
    button_back = tk.Button(completedScreen, font=("Nanito Sans", 10, "bold"), command=lambda: back(completedScreen), text="Zurück zum Start", background = "#b8aea6", foreground = "#1d1d1d", activebackground="#b8aea6", activeforeground = "white",highlightthickness=2, highlightbackground="#b8aea6", highlightcolor = "white", width=20, height=2, border=0, cursor="hand2")
    button_back.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    """Funktionen"""
    icon_show(completedScreen)
    startScreen.lower(completedScreen)

#Funktion die die PDFs zusammenfügt
def mergeFiles(window_name, label_name, entry_name):
    #Fehlermeldung verstecken (falls diese noch angezeigt wird)
    label_name.place_forget()

    #Namen holen & kontrollieren ob dieser gültig ist
    newFilename = entry_name.get()
    if any(char in newFilename for char in ["\\", "/", ":", "*", "?", "\"", "<", ">", "¦"]):
        label_name.place(relx=0.5, rely=0.95, anchor=tk.CENTER)
        return
        
    #PDFs zusammenfügen
    merger = PdfWriter()

    for pdf in filenames:
        merger.append(pdf)

    merger.write(newFilename+".pdf") #Namen geben
    merger.close()

    filenames.clear()
    sleep(1)
    window_name.destroy()
    functionFinished("PDFs wurden erfolgreich zusammengefügt!")

#Funkton PDF trennen
def splitFile(window_name, label_name1, label_name2, entry_name1, entry_name2, entry_name3):
    #Fehlermeldungen verstecken (falls diese noch angezeigt werden)
    label_name1.place_forget()
    label_name2.place_forget()

    #Namen holen & kontrollieren ob dieser gültig ist
    newFilename = entry_name1.get()
    if any(char in newFilename for char in ["\\", "/", ":", "*", "?", "\"", "<", ">", "¦"]):
        label_name2.place(relx=0.5, rely=0.85, anchor=tk.CENTER)
        return

    #Seitenbereiche holen und kontrollieren ob diese gültig sind
    #Kontrolle: Hat es Eingabe? & Ist Eingabe ein Integer?
    try:
        fromPage = int(entry_name2.get())
        toPage = int(entry_name3.get())
    except:
        label_name1.place(relx=0.5, rely=0.85, anchor=tk.CENTER)
        return
    
    #Kontrolle: Seitenbereich möglich? (Start < Ziel)
    if fromPage > toPage:
        label_name1.place(relx=0.5, rely=0.85, anchor=tk.CENTER)
        return

    if fromPage < 0:
        label_name1.place(relx=0.5, rely=0.85, anchor=tk.CENTER)
        return
    
    #Kontrolle: Seitenbereich grösser als PDF?
    def lengthPDF():
        pdf = open(filenames[0], "rb")
        reader = PdfReader(pdf)
        numberOfPages = len(reader.pages)
        return numberOfPages
        
    lenPDF = lengthPDF()
    if toPage > lenPDF:
        label_name1.place(relx=0.5, rely=0.85, anchor=tk.CENTER)
        return

    #PDF trennen
    merger = PdfWriter()
    pdf = open(filenames[0], "rb")
    merger.append(fileobj=pdf, pages=(fromPage-1,toPage))

    merger.write(newFilename+".pdf")
    merger.close()

    filenames.clear()
    sleep(1)
    window_name.destroy()
    functionFinished("PDF wurde erfolgreich getrennt!")


"""Zusammenfügen"""
def merge():
    """Fenster erstellen"""
    mergeScreen = tk.Tk()
    mergeScreen.geometry('750x500')
    mergeScreen.resizable(False, False)
    mergeScreen.configure(background='#f6f6f6')
    mergeScreen.title("PDF zusammenfügen")

    """Labels"""
    #Titel "PDF zusammenfügen"
    label_title = tk.Label(mergeScreen, text="PDF zusammenfügen", font=("Nunito Sans", 20, "bold"), fg="#1d1d1d",bg='#f6f6f6')
    label_title.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

    #Anweisung "Dateien hochladen (nur .pdf-Dateien):"
    label_instruction = tk.Label(mergeScreen, text="Dateien hochladen (nur .pdf-Dateien):", font=("Nunito Sans", 13, "bold"),fg="#1d1d1d", bg='#f6f6f6')
    label_instruction.place(relx=0.5, rely=0.225, anchor=tk.CENTER)

    #Untertitel "Ausgewählte Dateien:"
    label_subtitle = tk.Label(mergeScreen, text="Ausgewählte Dateien:", font=("Nunito Sans", 10, "bold"),fg="#1d1d1d", bg='#f6f6f6')
    label_subtitle.place(relx=0.45, rely=0.4, anchor=tk.CENTER)

    #Dateien anzeigen
    label_fileNames = tk.Label(mergeScreen, text=" ", font=("Nunito Sans", 10, "bold"),fg="#1d1d1d", bg='#f6f6f6')
    label_fileNames.place(relx=0.45, rely=0.55, anchor=tk.CENTER)

    #Ungültige Eingabe Name
    label_invalidName = tk.Label(mergeScreen, text="Ungültiger Name!", font=("Nunito Sans", 13, "bold"),fg="RED", bg='#f6f6f6')

    #Anweisung Name neues PDF
    label_newFilename = tk.Label(mergeScreen, text="Name des zusammengefügten PDF's:\n(Name darf keines dieser Zeichen enthalten: \/:*?\"<>¦)", font=("Nunito Sans", 10, "bold"),fg="#1d1d1d", bg='#f6f6f6')
    label_newFilename.place(relx=0.5, rely=0.85, anchor=tk.CENTER)

    """Entry-Widgets"""
    entry_newFilenme = tk.Entry(mergeScreen, width=50,  font=("Nunito Sans", 10), bg='white', fg='black')
    entry_newFilenme.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

    """Buttons"""
    #Button Dateien zusammenfügen
    button_mergeFiles = tk.Button(mergeScreen, font=("Nanito Sans", 10, "bold"), command=lambda: mergeFiles(mergeScreen, label_invalidName, entry_newFilenme), text="Zusammenfügen!", background = "#b8aea6", foreground = "#1d1d1d", activebackground="#b8aea6", activeforeground = "white",highlightthickness=2, highlightbackground="#b8aea6", highlightcolor = "white", width=20, height=2, border=0, cursor="hand2")
    button_mergeFiles.place(relx=0.85, rely=0.5, anchor=tk.CENTER)
    button_mergeFiles.config(state="disabled")

    #Button Dateien Auswählen
    button_chooseFiles = tk.Button(mergeScreen, font=("Nanito Sans", 10, "bold"), command=lambda: chooseFiles(mergeScreen, label_fileNames, button_mergeFiles, 1), text="Datei Auswählen", background = "#b8aea6", foreground = "#1d1d1d", activebackground="#b8aea6", activeforeground = "white",highlightthickness=2, highlightbackground="#b8aea6", highlightcolor = "white", width=20, height=2, border=0, cursor="hand2")
    button_chooseFiles.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

    #Button Dateien löschen
    button_deleteFiles = tk.Button(mergeScreen, font=("Nanito Sans", 10, "bold"), command=lambda: deleteFiles(label_fileNames, button_mergeFiles, 1), text="Eingabe zurücksetzen", background = "#b8aea6", foreground = "#1d1d1d", activebackground="#b8aea6", activeforeground = "white",highlightthickness=2, highlightbackground="#b8aea6", highlightcolor = "white", width=20, height=2, border=0, cursor="hand2")
    button_deleteFiles.place(relx=0.5, rely=0.725, anchor=tk.CENTER)

    #Button zurück zum Start
    button_back = tk.Button(mergeScreen, font=("Nanito Sans", 10, "bold"), command=lambda: back(mergeScreen), text="Zurück", background="#f6f6f6", foreground="#1d1d1d", activebackground="#f6f6f6", activeforeground="white", highlightthickness=2, highlightbackground="#f6f6f6", highlightcolor="white", width=20, height=2, border=0, cursor="hand2")
    button_back.place(relx=0.1, rely=0.15, anchor=tk.CENTER)


    """Funktionen"""
    #Als Strings?
    icon_show(mergeScreen)

    """Mainloop"""
    mergeScreen.mainloop()


"""Trennen"""
def split():
    """Fenster"""
    splitScreen = tk.Tk()
    splitScreen.geometry('750x500')
    splitScreen.resizable(False, False)
    splitScreen.configure(background='#f6f6f6')
    splitScreen.title("PDF trennen")

    """Labels"""
    #Titel "PDF trennen"
    label_title = tk.Label(splitScreen, text="PDF trennen", font=("Nunito Sans", 20, "bold"), fg="#1d1d1d",bg='#f6f6f6')
    label_title.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

    #Anweisung "Datei hochladen (nur .pdf-Datei):"
    label_instruction = tk.Label(splitScreen, text="Datei hochladen (nur .pdf-Datei):", font=("Nunito Sans", 13, "bold"),fg="#1d1d1d", bg='#f6f6f6')
    label_instruction.place(relx=0.5, rely=0.225, anchor=tk.CENTER)

    #Ausgewählte Datei "Ausgewählte Datei:"
    label_subtitle = tk.Label(splitScreen, text="Ausgewählte Datei:", font=("Nunito Sans", 10, "bold"),fg="#1d1d1d", bg='#f6f6f6')
    label_subtitle.place(relx=0.5, rely=0.375, anchor=tk.CENTER)

    #Ausgewählte Datei anzeigen
    label_fileNames = tk.Label(splitScreen, text=" ", font=("Nunito Sans", 10, "bold"),fg="#1d1d1d", bg='#f6f6f6')
    label_fileNames.place(relx=0.5, rely=0.425, anchor=tk.CENTER)

    #Bereiche die getrennt werden sollen
    label_subtitle2 = tk.Label(splitScreen, text="PDF nach Seitenbereiche trennen", font=("Nunito Sans", 13, "bold"),fg="#1d1d1d", bg='#f6f6f6')
    label_subtitle2.place(relx=0.5, rely=0.625, anchor=tk.CENTER)

    #Seitenbereich eingeben
    label_instruction2 = tk.Label(splitScreen, text="Von Seite", font=("Nunito Sans", 10, "bold"),fg="#1d1d1d", bg='#f6f6f6')
    label_instruction2.place(relx=0.4, rely=0.675, anchor=tk.E)

    label_instruction3 = tk.Label(splitScreen, text="bis Seite", font=("Nunito Sans", 10, "bold"),fg="#1d1d1d", bg='#f6f6f6')
    label_instruction3.place(relx=0.6, rely=0.675, anchor=tk.E)

    #Anweisung Name neues PDF
    label_newFilename = tk.Label(splitScreen, text="Name des zusammengefügten PDF's:\n(Name darf keines dieser Zeichen enthalten: \/:*?\"<>¦)", font=("Nunito Sans", 10, "bold"),fg="#1d1d1d", bg='#f6f6f6')
    label_newFilename.place(relx=0.5, rely=0.75, anchor=tk.CENTER)

    #Ungültige Eingabe Seitenbereich
    label_invalidInput = tk.Label(splitScreen, text="Ungültiger Seitenbereich!", font=("Nunito Sans", 13, "bold"),fg="RED", bg='#f6f6f6')

    #Ungültige Eingabe Name
    label_invalidName = tk.Label(splitScreen, text="Ungültiger Name!", font=("Nunito Sans", 13, "bold"),fg="RED", bg='#f6f6f6')

    """Entry-Widgets"""
    #Neuer Name
    entry_newFilenme = tk.Entry(splitScreen, width=50,  font=("Nunito Sans", 10), bg='white', fg='black')
    entry_newFilenme.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

    #Seitenbereich eingeben
    entry_from = tk.Entry(splitScreen, width=10,  font=("Nunito Sans", 10), bg='white', fg='black') #Feld zum reinschreiben.
    entry_from.place(relx=0.4, rely=0.675, anchor=tk.W)

    entry_to = tk.Entry(splitScreen, width=10,  font=("Nunito Sans", 10), bg='white', fg='black') #Feld zum reinschreiben.
    entry_to.place(relx=0.6, rely=0.675, anchor=tk.W)

    """Buttons"""
    #Button Dateien trennen
    button_splitFile = tk.Button(splitScreen, font=("Nanito Sans", 10, "bold"), command=lambda: splitFile(splitScreen, label_invalidInput, label_invalidName, entry_newFilenme, entry_from, entry_to), text="Trennen!", background = "#b8aea6", foreground = "#1d1d1d", activebackground="#b8aea6", activeforeground = "white",highlightthickness=2, highlightbackground="#b8aea6", highlightcolor = "white", width=20, height=2, border=0, cursor="hand2")
    button_splitFile.place(relx=0.5, rely=0.925, anchor=tk.CENTER)
    button_splitFile.config(state="disabled")

    #Button Dateien Auswählen
    button_chooseFiles = tk.Button(splitScreen, font=("Nanito Sans", 10, "bold"), command=lambda: chooseFiles(splitScreen, label_fileNames, button_splitFile, 2, button_chooseFiles), text="Datei Auswählen", background = "#b8aea6", foreground = "#1d1d1d", activebackground="#b8aea6", activeforeground = "white",highlightthickness=2, highlightbackground="#b8aea6", highlightcolor = "white", width=20, height=2, border=0, cursor="hand2")
    button_chooseFiles.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

    #Button Dateien löschen
    button_deleteFiles = tk.Button(splitScreen, font=("Nanito Sans", 10, "bold"), command=lambda: deleteFiles(label_fileNames, button_splitFile, 2, button_chooseFiles), text="Eingabe zurücksetzen", background = "#b8aea6", foreground = "#1d1d1d", activebackground="#b8aea6", activeforeground = "white",highlightthickness=2, highlightbackground="#b8aea6", highlightcolor = "white", width=20, height=2, border=0, cursor="hand2")
    button_deleteFiles.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    #Button zurück zum Start
    button_back = tk.Button(splitScreen, font=("Nanito Sans", 10, "bold"), command=lambda: back(splitScreen), text="Zurück", background="#f6f6f6", foreground="#1d1d1d", activebackground="#f6f6f6", activeforeground="white", highlightthickness=2, highlightbackground="#f6f6f6", highlightcolor="white", width=20, height=2, border=0, cursor="hand2")
    button_back.place(relx=0.1, rely=0.15, anchor=tk.CENTER)

    """Funktionen"""
    icon_show(splitScreen)

    """Mainloop"""
    splitScreen.mainloop()


"""Start"""
#Fenster erstellen
startScreen = tk.Tk()
startScreen.geometry('750x500')
startScreen.resizable(False, False)
startScreen.configure(background='#f6f6f6')
startScreen.title("Start PDF Bearbeitungstool")

"""Labels"""
#Titel "PDF Bearbeitungstool"
label_title = tk.Label(startScreen, text="PDF Bearbeitungtool", font=("Nunito Sans", 20, "bold"), fg="#1d1d1d",bg='#f6f6f6')
label_title.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

#"Tools"
label_subtitle = tk.Label(startScreen, text="Tools:", font=("Nunito Sans", 15, "bold"),fg="#1d1d1d", bg='#f6f6f6')
label_subtitle.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

"""Buttons"""
#Button PDF Zusammenfügen
button_merge = tk.Button(startScreen, font=("Nanito Sans", 10, "bold"), command= lambda:merge(), text="PDFs zusammenfügen", background = "#b8aea6", foreground = "#1d1d1d", activebackground="#b8aea6", activeforeground = "white",highlightthickness=2, highlightbackground="#b8aea6", highlightcolor = "white", width=30, height=2, border=0, cursor="hand2")
button_merge.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

#Button PDF Trennen
button_split = tk.Button(startScreen, font=("Nanito Sans", 10, "bold"), command= lambda:split(), text="PDF trennen", background = "#b8aea6", foreground = "#1d1d1d", activebackground="#b8aea6", activeforeground = "white",highlightthickness=2, highlightbackground="#b8aea6", highlightcolor = "white", width=30, height=2, border=0, cursor="hand2")
button_split.place(relx=0.5, rely=0.625, anchor=tk.CENTER)

"""Funktionen"""
icon_show(startScreen)

startScreen.mainloop()
