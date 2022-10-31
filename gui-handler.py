# Wouter Missler, 2022
# Zorgt voor alle GUI elementen en stuurt het door naar de juiste functies.

import tkinter as tk

# globale variabelen
_kleuren = {
    "nsGeel": "#FFC917",
    "nsBlauw": "#003082",
    "Achtergrond": "#FFFFFF"
}

# GUI basis
root = tk.Tk()  # initialiseer tkinter
root.title("NS")  # placeholder titel
root.geometry("1000x600")  # zet de grootte van de GUI vast
root.resizable(0, 0)  # zorgt ervoor dat de window niet geresized kan worden
root.configure(bg=_kleuren["nsBlauw"])  # achtergrondkleur van de GUI


def logoGUI():
    '''Zorgt voor het logo van de ns aan de bovenkant van het scherm'''

    # maak een frame aan
    logoFrame = tk.Frame(root, bg=_kleuren["nsGeel"], height=100)
    logoFrame.pack(fill=tk.X)

    # voeg een label toe aan de frame
    logoLabel = tk.Label(logoFrame, text=root.title(),
                         bg=_kleuren["nsGeel"], fg=_kleuren["nsBlauw"], font=("Helvetica", 20, "bold"))
    logoLabel.pack(pady=20)


def mainGUI():
    '''Zorgt voor de template GUI van het stationszuil'''

    # voeg het logo toe
    logoGUI()


def zuilGUI():
    '''Zorgt voor de GUI van de zuil module van het stationszuil, voegt de benodigde inputvelden toe en een manier om die door te geven'''

    # set de titel
    root.title("Zuil NS")

    # roep de boilerplate GUI aan
    mainGUI()

    # maak een frame met daarin twee labels en twee entry velden, voor de naam en het bericht van de gebruiker
    zuilFrame = tk.Frame(
        root, bg=_kleuren["nsGeel"], padx=20, pady=20, height=300)
    zuilFrame.pack(pady=130)

    # configureer het grid van de frame (3 rijen, 2 kolommen)
    zuilFrame.columnconfigure(0, weight=1)  # labels hebben 1/4 van de breedte
    # entry velden hebben 3/4 van de breedte
    zuilFrame.columnconfigure(1, weight=2)

    # voeg de labels toe
    naamLabel = tk.Label(zuilFrame, text="Naam:", bg=_kleuren["nsGeel"], fg=_kleuren["nsBlauw"], font=(
        "Helvetica", 15))
    naamLabel.grid(row=0, column=0, padx=10, pady=10)

    berichtLabel = tk.Label(zuilFrame, text="Bericht:",
                            bg=_kleuren["nsGeel"], fg=_kleuren["nsBlauw"], font=("Helvetica", 15))
    berichtLabel.grid(row=1, column=0, padx=10, pady=10)

    # voeg de text velden toe
    naamText = tk.Text(zuilFrame, width=30, height=1, font=(
        "Helvetica", 12), bg=_kleuren["nsBlauw"], fg=_kleuren["Achtergrond"])
    naamText.grid(row=0, column=1, padx=10, pady=15)

    berichtText = tk.Text(zuilFrame, width=30, height=5,
                          font=("Helvetica", 12), bg=_kleuren["nsBlauw"], fg=_kleuren["Achtergrond"])
    berichtText.grid(row=1, column=1, padx=10, pady=15)

    # voeg een knop toe om het bericht door te geven
    submitButton = tk.Button(zuilFrame, text="Verstuur",
                             bg=_kleuren["nsBlauw"], fg=_kleuren["Achtergrond"], font=("Helvetica", 15), relief=tk.GROOVE)
    submitButton.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    # roep de main loop aan
    root.mainloop()
