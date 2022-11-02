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


def clearGUI():
    '''Maakt GUI leeg'''

    for widget in root.winfo_children():
        widget.destroy()

    mainGUI()


def logoGUI():
    '''Zorgt voor het logo van de ns aan de bovenkant van het scherm'''

    # maak een frame aan
    logoFrame = tk.Frame(root, bg=_kleuren["nsGeel"], height=100)
    logoFrame.pack(fill=tk.X)

    # voeg een label toe aan de frame
    logoLabel = tk.Label(logoFrame, text=root.title(),
                         bg=_kleuren["nsGeel"], fg=_kleuren["nsBlauw"], font=("Helvetica", 25, "bold"))
    logoLabel.pack(pady=20)


def popupGUI(popupTitel, popupTekst):
    '''Zorgt voor de GUI van een simpele popup'''

    # maak een frame aan
    popupFrame = tk.Frame(
        root, bg=_kleuren["nsGeel"], padx=0, pady=0, height=300)
    popupFrame.pack(pady=(70, 0))

    # voeg een titel label toe aan de frame
    popupLabel = tk.Label(popupFrame, text=popupTitel, pady=20, padx=100, bg=_kleuren["Achtergrond"], fg=_kleuren["nsBlauw"], font=(
        "Helvetica", 18, "bold"))  # titel
    popupLabel.pack(pady=(0, 20), fill=tk.X)

    # voeg een tekst label toe aan de frame
    popupTekstLabel = tk.Label(popupFrame, text=popupTekst, pady=20, width=50, wraplength=400, bg=_kleuren["nsGeel"], fg=_kleuren["nsBlauw"], font=(
        "Helvetica", 12))  # tekst
    popupTekstLabel.pack(pady=(0, 20))

    # roep de main loop aan
    root.mainloop()


def mainGUI():
    '''Zorgt voor de template GUI van het stationszuil'''

    # voeg het logo toe
    logoGUI()


def zuilGUI(huidigStation, submitFunctie):
    '''Zorgt voor de GUI van de zuil module van het stationszuil, voegt de benodigde inputvelden toe en een manier om die door te geven'''

    # set de titel
    root.title("Zuil NS - Station {}".format(huidigStation))

    # roep de boilerplate GUI aan
    clearGUI()

    # maak een frame met daarin twee labels en twee entry velden, voor de naam en het bericht van de gebruiker
    zuilFrame = tk.Frame(
        root, bg=_kleuren["nsGeel"], padx=0, pady=0, height=300)
    zuilFrame.pack(pady=(70, 0))

    # configureer het grid van de frame (3 rijen, 2 kolommen)
    zuilFrame.columnconfigure(0, weight=1)  # labels hebben 1/4 van de breedte
    # entry velden hebben 3/4 van de breedte
    zuilFrame.columnconfigure(1, weight=2)

    # voeg de labels toe
    zuilTitel = tk.Label(zuilFrame, text="Laat uw opmerking hier achter!", pady=20, padx=100, bg=_kleuren["Achtergrond"], fg=_kleuren["nsBlauw"], font=(
        "Helvetica", 18, "bold"))  # titel
    zuilTitel.grid(row=0, column=0, columnspan=2, pady=(0, 20))

    naamLabel = tk.Label(zuilFrame, text="Naam:", padx=20, bg=_kleuren["nsGeel"], fg=_kleuren["nsBlauw"], font=(
        "Helvetica", 15))
    naamLabel.grid(row=1, column=0, pady=10)

    berichtLabel = tk.Label(zuilFrame, text="Bericht:", padx=20,
                            bg=_kleuren["nsGeel"], fg=_kleuren["nsBlauw"], font=("Helvetica", 15))
    berichtLabel.grid(row=2, column=0, pady=10)

    # voeg de text velden toe
    naamText = tk.Text(zuilFrame, width=30, height=1, font=(
        "Helvetica", 12), bg=_kleuren["nsBlauw"], fg=_kleuren["Achtergrond"])
    naamText.grid(row=1, column=1, pady=15)

    berichtText = tk.Text(zuilFrame, width=30, height=5,
                          font=("Helvetica", 12), bg=_kleuren["nsBlauw"], fg=_kleuren["Achtergrond"])
    berichtText.grid(row=2, column=1, pady=15)

    # voeg een knop toe om het bericht door te geven
    submitButton = tk.Button(zuilFrame, text="Verstuur",
                             bg=_kleuren["nsBlauw"], fg=_kleuren["Achtergrond"], font=("Helvetica", 15), relief=tk.GROOVE,
                             command=lambda: submitFunctie(naamText.get("1.0", "end-1c"), berichtText.get("1.0", "end-1c")))
    submitButton.grid(row=3, column=0, columnspan=2,
                      pady=20)

    # roep de main loop aan
    root.mainloop()
