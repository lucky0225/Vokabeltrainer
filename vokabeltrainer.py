import random


"""
Verbesserungen
    Speichern der Vokabeln in .text o.ä. (siehe firefox projekt)
        Import von Vokabeln (ggf. automatisch aktualisieren)
        versch. db f. versch. Sprachen
"""


class Entry:
    def __init__(self, deutsch, englisch):
        self.deutsch = deutsch
        self.englisch = englisch
    def toString(self):
        return self.deutsch + " - " + self.englisch
        
eintraege = [Entry("hallo", "hello")]

def eingabe():
    print("Tippe '#fertig' um die Eingabe der Vokabeln temporär zu speichern und zu beenden")
    while True:
        deutsch = input("Deutsches Wort: ")
        if deutsch == "#fertig":
            return
        englisch = input("Englisches Wort: ")
        if englisch == "#fertig":
            return
        eintraege.append(Entry(deutsch, englisch))
        
def abfrage():
    print("Tippe '#fertig' um die Eingabe der Vokabeln temporär zu speichern und zu beenden")
    while True:
        i = random.randint(0, len(eintraege)-1)
        englisch = input("Englische Übersetzung von " + eintraege[i].deutsch + ": ")
        if(englisch == "#fertig"):
            return
        if eintraege[i].englisch == englisch:
            print("korrekt!")
        else:
            print("leider falsch! Richtige Antwort: " + eintraege[i].englisch)

def beenden():
    print("Skript beendet")
    quit()

def printall():
    for eintrag in eintraege:
        print(eintrag.toString())
        

while True:
    print("""
    Verfügbare Befehle:
        eingabe
        abfrage
        beenden
    """)
    befehl = input("Befehl: ")
    if befehl == "eingabe":
        eingabe()
    elif befehl == "abfrage":
        abfrage()
    elif befehl == "beenden":
        beenden()
    else:
        print("keine bekannte Ausgabe. Tippe: eingabe, abfrage, ausgabe oder beenden.")
    