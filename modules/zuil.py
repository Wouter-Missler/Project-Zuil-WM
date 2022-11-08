# Wouter Missler, 2022
# Haalt input van gebruiker en stuurt het door naar de database, om zo gemodereerd te worden.

# Importeren van de benodigde modules
import random
from datetime import datetime

# Importeren van de project modules
from handlers import sql_handler as sql
from handlers import gui_handler as gui

# globale variabelen
alleStations = sql.fetchQuery("SELECT naam FROM station")  # alle stations
huidigStation = random.choice(alleStations)[0]  # willerkeurig station


def stuurBericht(naam, bericht):
    '''
    Haalt de input van de reiziger op en stuurt het door naar de database, om zo gemodereerd te worden.

    Parameters: naam (string): De naam van de reiziger
                bericht (string): Het bericht van de reiziger

    Returns: None
    '''

    # verifieer of het bericht binnen de limiet van 140 karakters valt
    if len(bericht) > 140:
        gui.errorGUI("Het bericht mag niet langer zijn dan 140 karakters.")
        return

    # als er geen naam is ingevuld, geef de reiziger de naam Anoniem
    if (naam == ""):
        naam = "Anoniem"

    # als het bericht leeg is, geef een error en return
    if (bericht == ""):
        gui.errorGUI("Het bericht mag niet leeg zijn.")
        return

    # haal de huidige tijd en datum op
    now = datetime.now()
    datumStr = str(now.strftime("%d-%m-%Y"))
    tijdStr = str(now.strftime("%H:%M:%S"))

    # voeg de input toe aan de database
    sql.commitQuery(
        "INSERT INTO bericht (naam,bericht,datum,tijd,station,goedgekeurd,moderator) VALUES (%s, %s, %s, %s, %s,%s,%s)", (naam.strip(), bericht.strip(), datumStr, tijdStr, huidigStation, "0", "1"))

    # laat een popup zien dat het bericht is verstuurd
    gui.clearGUI()
    gui.popupGUI("Bericht verstuurd",
                 "Uw bericht is verstuurd naar het moderatie-team van " + huidigStation + "." + " Uw bericht wordt zo spoedig mogelijk bekeken.")


def start():
    '''Start het zuil scherm waar een bericht ingevuld kan worden'''

    gui.initGUI()  # initialiseer de GUI

    gui.zuilGUI(huidigStation, stuurBericht)  # start de GUI
