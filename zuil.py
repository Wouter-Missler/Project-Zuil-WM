# Wouter Missler, 2022
# Haalt input van gebruiker en stuurt het door naar een csv bestand, om zo gemodereerd te worden.

# Importeren van de benodigde modules
import random
from datetime import datetime

# Importeren van de project modules
import sql_handler as sql
import gui_handler as gui

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

    # haal de huidige tijd en datum op
    now = datetime.now()
    datumStr = str(now.strftime("%d-%m-%Y"))
    tijdStr = str(now.strftime("%H:%M:%S"))

    # voeg de input toe aan de database
    sql.insertQuery(
        "INSERT INTO bericht (naam,bericht,datum,tijd,station) VALUES (%s, %s, %s, %s, %s)", (naam, bericht, datumStr, tijdStr, huidigStation))

    # laat een popup zien dat het bericht is verstuurd
    gui.clearGUI()
    gui.popupGUI("Bericht verstuurd",
                 "Uw bericht is verstuurd naar het moderatie-team van " + huidigStation + "." + " Uw bericht wordt zo spoedig mogelijk bekeken.")


gui.zuilGUI(huidigStation, stuurBericht)  # start de GUI

# -----------------------------------------------------------------
#                          test code
# -----------------------------------------------------------------

# simpele query test die alle berichteninfo ophaalt en als een tabel print
# query = "SELECT * FROM bericht"
# # parameters = ["Gouda"]
# records = sql.fetchQuery(query)

# print("{0:15} | {1:15} | {2:15} | {3:15} | {4:15} | {5:15}".format(
#     "Nummer", "Bericht", "Datum", "Tijd", "Naam", "Station"))
# print("----------------------------------------------------------------------------------------------------------------------------------")

# for record in records:
#     # print(record)
#     print("{0:15} | {1:15} | {2:15} | {3:15} | {4:15} | {5:15}".format(
#         record[0], record[1], str(record[2]), str(record[3]), record[4], record[5]))
