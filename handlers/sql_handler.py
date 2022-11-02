# Wouter Missler, 2022
# Zorgt voor de verbindingen met de Database en de queries die daarop uitgevoerd worden.

# Importeren van de benodigde modules
import psycopg2

# De connectie string voor de database
connection_string = "host='localhost' dbname='Project-Stationszuil' user='postgres' password='1234'"


def fetchQuery(query, parameters=None):
    '''
    Voert een query uit op de database en geeft het resultaat terug

    Parameters: query (string): De query die uitgevoerd moet worden
                parameters (list): De parameters die gebruikt moeten worden in de query

    Returns: records (list met tuples): De resultaten van de query
    '''

    # De connectie met de database
    conn = psycopg2.connect(connection_string)
    cur = conn.cursor()

    # Het uitvoeren van de query
    cur.execute(query, parameters)
    records = cur.fetchall()
    conn.close()

    # Het teruggeven van de resultaten
    return records


def commitQuery(query, parameters=None):
    '''
    Voert een query uit op de database om data toe te voegen

    Parameters: query (string): De query die uitgevoerd moet worden
                parameters (list): De parameters die gebruikt moeten worden in de query

    Returns: None
    '''

    # De connectie met de database
    conn = psycopg2.connect(connection_string)
    cur = conn.cursor()

    # Het uitvoeren van de query
    cur.execute(query, parameters)
    conn.commit()  # commit de veranderingen
    conn.close()
