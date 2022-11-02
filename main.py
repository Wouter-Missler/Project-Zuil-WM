# Wouter Missler, 2022
# Hoofdbestand dat de verschillende modules aanroept

# Importeren van de project modules
from modules import zuil
from modules import moderatie
from modules import stationshal


def main():
    '''
    Het hoofdmenu van het project. Hier kan de gebruiker kiezen tussen de verschillende modules.
    '''

    # vraag welk bestand er moet worden uitgevoerd
    choice = input(
        "Kies een optie: \n1. Stationshal \n2. Moderatie \n3. Stationszuil \n")

    # voer het gekozen bestand uit
    if choice == "1":
        stationshal.start()
    elif choice == "2":
        moderatie.start()
    elif choice == "3":
        zuil.start()
    else:
        # laat een error zien
        print("\033c")  # clear de console
        print("Ongeldige keuze. Probeer het opnieuw.")
        main()


print("\033c")  # clear de console
print("Welkom bij de stationszuil. ", end="")
main()
