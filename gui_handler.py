# Wouter Missler, 2022
# Zorgt voor alle GUI elementen en stuurt het door naar de juiste functies.

import tkinter as tk

# globale variabelen
_kleuren = {
    "nsGeel": "#FFC917",
    "nsBlauw": "#003082",
    "Error": "#DE2044",
    "Achtergrond": "#FFFFFF",
    "AchtergrondDonker": "#ECECEC"
}

# GUI basis
root = tk.Tk()  # initialiseer tkinter
root.title("NS")  # placeholder titel
root.geometry("1000x650")  # zet de grootte van de GUI vast
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


def errorGUI(popupTekst):
    '''Zorgt voor de GUI van een error popup die absoluut gepositioneerd is rechtsonderaan het scherm'''

    # maak een frame aan
    popupFrame = tk.Frame(
        root, bg=_kleuren["Error"], padx=0, pady=0, height=300)
    popupFrame.place(x=1000, y=650, anchor="se")

    # voeg een tekst label toe aan de frame
    popupTekstLabel = tk.Label(popupFrame, text=popupTekst, pady=20, width=30, wraplength=200, bg=_kleuren["Error"], fg=_kleuren["Achtergrond"], font=(
        "Helvetica", 8, "bold"))  # tekst
    popupTekstLabel.pack()


def mainGUI():
    '''Zorgt voor de template GUI van het stationszuil'''

    # voeg het logo toe
    logoGUI()


def zuilGUI(huidigStation, submitFunctie):
    '''Zorgt voor de GUI van de zuil module van het stationszuil, voegt de benodigde inputvelden toe en een manier om die door te geven'''

    # set de titel
    root.title("NS - Station {}".format(huidigStation))

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


def moderatorLoginGUI(loginFunctie):
    '''Zorgt voor de GUI van de moderator login module van het stationszuil'''

    # set de titel
    root.title("NS - Moderator Login")

    # roep de boilerplate GUI aan
    clearGUI()

    # maak een frame met daarin twee labels en twee entry velden, voor de naam en het bericht van de gebruiker
    loginFrame = tk.Frame(
        root, bg=_kleuren["nsGeel"], padx=0, pady=0, height=300)
    loginFrame.pack(pady=(70, 0))

    # configureer het grid van de frame (3 rijen, 2 kolommen)
    loginFrame.columnconfigure(0, weight=1)  # labels hebben 1/4 van de breedte
    # entry velden hebben 3/4 van de breedte
    loginFrame.columnconfigure(1, weight=2)

    # voeg de labels toe
    zuilTitel = tk.Label(loginFrame, wraplength=400, text="Welkom, log hieronder in om te beginnen met het modereren van berichten.", pady=20, padx=100, bg=_kleuren["Achtergrond"], fg=_kleuren["nsBlauw"], font=(
        "Helvetica", 18, "bold"))  # titel
    zuilTitel.grid(row=0, column=0, columnspan=2, pady=(0, 20))

    naamLabel = tk.Label(loginFrame, text="Email:", padx=20, bg=_kleuren["nsGeel"], fg=_kleuren["nsBlauw"], font=(
        "Helvetica", 15))
    naamLabel.grid(row=1, column=0, pady=10)

    berichtLabel = tk.Label(loginFrame, text="Wachtwoord:", padx=20,
                            bg=_kleuren["nsGeel"], fg=_kleuren["nsBlauw"], font=("Helvetica", 15))
    berichtLabel.grid(row=2, column=0, pady=10)

    # voeg de text velden toe
    emailText = tk.Entry(loginFrame, width=30, font=(
        "Helvetica", 12), bg=_kleuren["nsBlauw"], fg=_kleuren["Achtergrond"])
    emailText.grid(row=1, column=1, pady=15)

    wachtwoordText = tk.Entry(loginFrame, width=30, show="*",
                              font=("Helvetica", 12), bg=_kleuren["nsBlauw"], fg=_kleuren["Achtergrond"])
    wachtwoordText.grid(row=2, column=1, pady=15)

    # voeg een knop toe om in te loggen
    submitButton = tk.Button(loginFrame, text="Log in",
                             bg=_kleuren["nsBlauw"], fg=_kleuren["Achtergrond"], font=("Helvetica", 15), relief=tk.GROOVE,
                             command=lambda: loginFunctie(emailText.get(), wachtwoordText.get()))
    submitButton.grid(row=3, column=0, columnspan=2,
                      pady=20)

    # roep de main loop aan
    root.mainloop()


def moderatorGUI(teKeurenBericht, keurBerichtFunctie):
    '''Zorgt voor de GUI voor de moderator waarin het eerste bericht dat nog niet is goedgekeurd wordt weergegeven
    met de optie om het bericht te keuren of af te keuren'''

    # set de titel
    root.title("NS - Moderator")

    # roep de boilerplate GUI aan
    clearGUI()

    # maak een frame aan
    moderatorOverviewFrame = tk.Frame(
        root, bg=_kleuren["nsGeel"], padx=0, pady=0, height=300)
    moderatorOverviewFrame.pack(pady=(70, 0))

    # voeg een titel label toe aan de frame
    titelLabel = tk.Label(moderatorOverviewFrame, text="Bericht om te keuren:", pady=20, padx=150, bg=_kleuren["Achtergrond"], fg=_kleuren["nsBlauw"], font=(
        "Helvetica", 18, "bold"))  # titel
    titelLabel.grid(pady=(0, 20), row=0, column=0, columnspan=2)

    # voeg een label toe aan de frame met daarin de naam van de reiziger
    naamLabel = tk.Label(moderatorOverviewFrame, text="Geschreven door: " + teKeurenBericht[4], pady=20, padx=100, bg=_kleuren["nsGeel"], fg=_kleuren["nsBlauw"], font=(
        "Helvetica", 14, "bold"))
    naamLabel.grid(pady=(0, 10), row=1, column=0, columnspan=2)

    # voeg een text toe aan de frame met daarin het bericht dat nog niet is goedgekeurd
    textString = teKeurenBericht[1]
    berichtText = tk.Label(moderatorOverviewFrame, text=textString, pady=20, width=30, wraplength=200, bg=_kleuren["nsGeel"], fg=_kleuren["nsBlauw"], font=(
        "Helvetica", 12))  # tekst
    berichtText.grid(pady=(0, 20), row=2, column=0, columnspan=2)

    # voeg twee knoppen toe aan de frame, een om het bericht goed te keuren en een om het bericht af te keuren
    goedKeurenButton = tk.Button(moderatorOverviewFrame, text="Goedkeuren", bg=_kleuren["nsBlauw"], fg=_kleuren["Achtergrond"], font=("Helvetica", 15), relief=tk.GROOVE,
                                 command=lambda: keurBerichtFunctie(teKeurenBericht[0], True))
    goedKeurenButton.grid(row=3, column=0, pady=20)

    afKeurenButton = tk.Button(moderatorOverviewFrame, text="Afkeuren", bg=_kleuren["nsBlauw"], fg=_kleuren["Achtergrond"], font=("Helvetica", 15), relief=tk.GROOVE,
                               command=lambda: keurBerichtFunctie(teKeurenBericht[0], False))
    afKeurenButton.grid(row=3, column=1, pady=20)

    root.mainloop()


def stationsSelectieGUI(stations, selecteerStationFunctie):
    '''Zorgt voor de GUI voor het selecteren van een station waar het stationsscherm zal hangen'''

    # set de titel
    root.title("NS - Stationsselectie")

    # roep de boilerplate GUI aan
    clearGUI()

    # maak een frame aan
    stationsSelectieFrame = tk.Frame(
        root, bg=_kleuren["nsGeel"], padx=0, pady=0, height=300)
    stationsSelectieFrame.pack(pady=(70, 0))

    # voeg een titel label toe aan de frame
    titelLabel = tk.Label(stationsSelectieFrame, text="Selecteer een station:", pady=20, padx=100, bg=_kleuren["Achtergrond"], fg=_kleuren["nsBlauw"], font=(
        "Helvetica", 18, "bold"))
    titelLabel.grid(pady=(0, 20), row=0, column=0, columnspan=2)

    # voeg een optionmenu toe aan de frame met daarin alle stations
    stationString = tk.StringVar()
    stationString.set(stations[0])
    stationMenu = tk.OptionMenu(
        stationsSelectieFrame, stationString, *stations)
    stationMenu.config(bg=_kleuren["nsBlauw"], fg=_kleuren["Achtergrond"], font=(
        "Helvetica", 15), relief=tk.GROOVE)
    stationMenu.grid(row=1, column=0, columnspan=2, pady=20)

    # voeg een knop toe aan de frame om het station te selecteren
    selecteerButton = tk.Button(stationsSelectieFrame, text="Selecteer", bg=_kleuren["nsBlauw"], fg=_kleuren["Achtergrond"], font=("Helvetica", 15), relief=tk.GROOVE,
                                command=lambda: selecteerStationFunctie(eval(stationString.get())[0]))
    selecteerButton.grid(row=2, column=0, columnspan=2, pady=20)

    root.mainloop()


def stationsschermGUI(station, laatsteBerichten, lokaleTemp, faciliteiten):
    '''Zorgt voor de GUI voor het stationscherm waarin de 5 meest recente gemodereerde berichten worden weergegeven'''

    # set de titel
    root.title("NS - Stationscherm {}".format(station))

    # roep de boilerplate GUI aan
    clearGUI()

    # maak een label aan waarin de lokale temperatuur wordt weergegeven
    lokaleTempLabel = tk.Label(root, text="Lokale temperatuur: " + str(lokaleTemp) + "°C", pady=20, padx=100, bg=_kleuren["Achtergrond"], fg=_kleuren["nsBlauw"], font=(
        "Helvetica", 18, "bold"))
    lokaleTempLabel.pack(pady=(0, 0), fill=tk.X)

    # maak een frame aan met 5 kolommen
    stationschermFrame = tk.Frame(
        root, bg=_kleuren["nsBlauw"], padx=0, pady=0, height=300)
    stationschermFrame.pack(pady=(20, 0))

    # maak een loop waarin we door de laatste berichten gaan, dit hoeft niet 5 te zijn
    for i in range(len(laatsteBerichten)):
        huidigBericht = laatsteBerichten[i]  # pak het huidige bericht

        # maak een frame aan
        berichtFrame = tk.Frame(
            stationschermFrame, bg=_kleuren["nsGeel"], padx=0, pady=0, height=300, width=178)
        berichtFrame.grid(row=0, column=i, padx=10, sticky="N")

        # voeg een titel label toe aan de frame
        titelLabel = tk.Label(berichtFrame, text="{}:".format(huidigBericht[4]), pady=10, width=14, bg=_kleuren["Achtergrond"], fg=_kleuren["nsBlauw"], font=(
            "Helvetica", 15, "bold"))  # titel
        titelLabel.pack()

        # voeg een label toe met de stationsnaam van het bericht
        stationLabel = tk.Label(berichtFrame, text="Station: "+huidigBericht[5], pady=8, width=14, bg=_kleuren["AchtergrondDonker"], fg=_kleuren["nsBlauw"], font=(
            "Helvetica", 10, "bold"))  # station
        stationLabel.pack(fill=tk.X)

        # voeg een label toe aan de frame met daarin de tekst van het bericht
        berichtText = tk.Label(berichtFrame, text=huidigBericht[1], pady=10, width=14, wraplength=120, bg=_kleuren["nsGeel"], fg=_kleuren["nsBlauw"], font=(
            "Helvetica", 10))  # bericht
        berichtText.pack()

        # voeg een label toe aan de frame met faciliteiten:
        faciliteitenLabel = tk.Label(berichtFrame, text="Faciliteiten: ", pady=8, width=14, anchor='w', bg=_kleuren["nsGeel"], fg=_kleuren["nsBlauw"], font=(
            "Helvetica", 10, "bold"))  # faciliteiten
        faciliteitenLabel.pack(fill=tk.X, padx=10)

        # voeg een frame toe waarin de faciliteiten worden weergegeven
        faciliteitenFrame = tk.Frame(
            berichtFrame, bg=_kleuren["nsGeel"], padx=10, pady=0, height=100)
        faciliteitenFrame.pack(fill=tk.X)

        # maak een loop waarin we door de faciliteiten van het bericht gaan
        for faciliteitKey in faciliteiten[i]:
            # pak de faciliteit boolean
            faciliteit = faciliteiten[i][faciliteitKey]

            if (faciliteit):
                print("{}: {}".format(faciliteitKey, faciliteit))
                # maak een label aan met de faciliteit
                faciliteitImg = tk.PhotoImage(
                    file="./assets/img_{}.png".format(faciliteitKey))
                # resize de image to fit in 15x15
                faciliteitImg = faciliteitImg.subsample(4, 4)
                faciliteitLabel = tk.Label(
                    faciliteitenFrame, image=faciliteitImg, width=32, height=32)
                faciliteitLabel.image = faciliteitImg
                faciliteitLabel.pack(side=tk.LEFT, padx=2, pady=8)
