# Wouter Missler, 2022
# Zorgt voor de GUI van het stationsscherm, laat de berichten in chronologische volgorde zien.
# Alleen de laatste 5 berichten worden getoond.
# en laat daarbij de benodigde informatie zien via de weather api.

# Importeren van de benodigde modules
import requests
import math

# Importeren van de project modules
import gui_handler as gui
import sql_handler as sql

# globale variabelen
apiKey = "ea483d18a21474f2752841755af5f59c"
berichten = []


def krijgTemperatuur(stad, land):
    '''
    Haalt de temperatuur op van een stad via de weather api

    Parameters: stad (string): De stad waarvan de temperatuur opgehaald moet worden

    Returns: temperatuur (int): De temperatuur van de stad
    '''

    # haal de latitude en longitude op
    response = requests.get("http://api.openweathermap.org/geo/1.0/direct?q={},{}&limit=1&appid={}".format(
        stad, land, apiKey))
    lat = response.json()[0]['lat']
    lon = response.json()[0]['lon']

    # haal de temperatuur op
    response = requests.get(
        "https://api.openweathermap.org/data/2.5/weather?lat={}6&lon={}&appid={}".format(lat, lon, apiKey))
    temperatuur = response.json()['main']['temp']-273.15
    temperatuur = math.floor(temperatuur)

    return temperatuur


def selecteerStation(stad):
    '''
    Laat het stationsscherm zien voor een bepaald station

    Parameters: stad (string): De stad waarvan het stationsscherm moet worden geopend

    Returns: None
    '''
    print(stad)

    # haal de temperatuur op
    temperatuur = krijgTemperatuur(stad, "NL")

    # haal de laaste 5 berichten op die goed zijn gekeurd
    query = "SELECT * FROM bericht WHERE goedgekeurd = True ORDER BY datum DESC, tijd DESC LIMIT 5"
    berichten = sql.fetchQuery(query)

    # creeer een list met dictionaries van de faciliteiten per bericht
    faciliteiten = []

    for bericht in berichten:
        # zet faciliteiten om naar een dictionary
        query = "SELECT * FROM station WHERE naam = %s LIMIT 1"
        parameters = [bericht[5]]
        stationData = sql.fetchQuery(query, parameters)[0]
        faciliteitenDict = {
            "ovfiets": stationData[2],
            "lift": stationData[3],
            "wc": stationData[4],
            "pr": stationData[5]
        }

        # voeg de faciliteiten toe aan de list
        faciliteiten.append(faciliteitenDict)

    # open het stations scherm
    gui.stationsschermGUI(stad, berichten, temperatuur, faciliteiten)


# haal alle stations op
query = "SELECT naam FROM station"
records = sql.fetchQuery(query)

# laat de gebruiker een station kiezen waar het stationsscherm zal worden geopend
gui.stationsSelectieGUI(records, selecteerStation)
