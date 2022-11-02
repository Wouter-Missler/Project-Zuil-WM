# Wouter Missler, 2022
# Zorgt voor de interface van de moderators via de gui handler
# en zorgt ervoor dat gemodereerde berichten in de database updaten om zo in het stationsscherm te komen.

# Importeren van de benodigde modules


# Importeren van de project modules
import handlers.gui_handler as gui
import handlers.sql_handler as sql

# globale variabelen
huidigModeratorNummer = 0


def moderatorLoginCheck(email, wachtwoord):
    '''
    Kijkt of de ingevoerde gegevens overeenkomen met een moderator in de database

    Parameters: email (string): De email van de moderator
                wachtwoord (string): Het wachtwoord van de moderator

    Returns: True of False
    '''
    # haal alle gegevens van de moderator op
    query = "SELECT * FROM moderator WHERE email = %s AND wachtwoord = %s"
    parameters = [email, wachtwoord]
    records = sql.fetchQuery(query, parameters)

    # kijk of er een moderator is gevonden
    if len(records) == 0:
        return False
    else:
        # sla het moderator nummer op
        global huidigModeratorNummer
        huidigModeratorNummer = records[0][0]

        return True


def loginFunctie(email, wachtwoord):
    '''
    Zorgt ervoor dat er een moderator kan inloggen.
    Eerst wordt er gecheckt of de moderator in kan loggen,
    daarna wordt er een nieuwe GUI geopend.

    Parameters: email (string): De email van de moderator
                wachtwoord (string): Het wachtwoord van de moderator

    Returns: True of False
    '''
    # kijk of de ingevoerde gegevens overeenkomen met een moderator in de database
    if moderatorLoginCheck(email, wachtwoord):
        # haal het eerste te modereren bericht op, door te kijken of het een beoordelingsdatum heeft
        query = "SELECT * FROM bericht WHERE beoordelingsdatum IS NULL LIMIT 1"
        records = sql.fetchQuery(query)

        if (len(records) > 0):
            # open het moderatie scherm
            gui.moderatorGUI(records[0], updateBericht)
        else:
            # als er geen te modereren berichten zijn, geef een melding
            gui.clearGUI()
            gui.popupGUI("Geen berichten",
                         "Er zijn geen berichten meer om te modereren. Bedankt voor het modereren!")

    else:
        # geef een foutmelding
        gui.errorGUI(
            "De ingevoerde gegevens zijn niet correct. Probeer opnieuw.")


def updateBericht(berichtNummer, goedgekeurd):
    '''
    Update het bericht in de database, zodat het in het stationscherm komt.

    Parameters: berichtID (int): Het ID van het bericht
                goedgekeurd (int): 0 of 1, of het bericht goedgekeurd is

    Returns: None
    '''
    # update het moderator id
    query = "UPDATE bericht SET moderator = %s WHERE berichtnummer = %s"
    parameters = [huidigModeratorNummer, berichtNummer]
    sql.commitQuery(query, parameters)

    # update het bericht in de database
    query = "UPDATE bericht SET goedgekeurd = %s WHERE berichtnummer = %s"
    parameters = [goedgekeurd, berichtNummer]
    sql.commitQuery(query, parameters)

    # update de datum van de beoordeling
    query = "UPDATE bericht SET beoordelingsdatum = CURRENT_DATE WHERE berichtnummer = %s"
    parameters = [berichtNummer]
    sql.commitQuery(query, parameters)

    # update de tijd van de beoordeling
    query = "UPDATE bericht SET beoordelingstijd = CURRENT_TIME WHERE berichtnummer = %s"
    parameters = [berichtNummer]
    sql.commitQuery(query, parameters)

    # open het volgende bericht
    query = "SELECT * FROM bericht WHERE beoordelingsdatum IS NULL LIMIT 1"
    records = sql.fetchQuery(query)

    if (len(records) > 0):
        # open het moderatie scherm
        gui.moderatorGUI(records[0], updateBericht)
    else:
        # als er geen te modereren berichten zijn, geef een melding
        gui.clearGUI()
        gui.popupGUI("Geen berichten",
                     "Er zijn geen berichten meer om te modereren. Bedankt voor het modereren!")


def start():
    '''Start het moderatie scherm'''

    gui.initGUI()  # initialiseer de GUI

    gui.moderatorLoginGUI(loginFunctie)
