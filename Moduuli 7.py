#Teht 1

def kuukauden_vuodenaika():
    vuodenajat = ("talvi", "talvi", "kevät", "kevät", "kevät", "kesä",
                  "kesä", "kesä", "syksy", "syksy", "syksy", "talvi")

    try:
        kuukausi = int(input("Anna kuukauden numero (1-12): "))
        if 1 <= kuukausi <= 12:
            print(f"Vuodenaika: {vuodenajat[kuukausi - 1]}")
        else:
            print("Virhe: Syötä numero väliltä 1-12.")
    except ValueError:
        print("Virhe: Syötä kelvollinen numero.")


kuukauden_vuodenaika()

#Teht 2

def nimien_tallennus():
    nimet = set()

    while True:
        nimi = input("Syötä nimi (tyhjä lopettaa): ").strip()
        if nimi == "":
            break
        elif nimi in nimet:
            print("Aiemmin syötetty nimi")
        else:
            print("Uusi nimi")
            nimet.add(nimi)

    print("\nSyötetyt nimet:")
    for n in nimet:
        print(n)


nimien_tallennus()

#Teht 3

def lentoasema_tiedot():
    lentoasemat = {}

    while True:
        print("\nValitse toiminto:")
        print("1) Lisää lentoasema")
        print("2) Hae lentoasema")
        print("3) Lopeta")
        valinta = input("Anna valinta (1-3): ").strip()

        if valinta == "1":
            icao = input("Anna lentoaseman ICAO-koodi: ").strip().upper()
            nimi = input("Anna lentoaseman nimi: ").strip()
            lentoasemat[icao] = nimi
            print("Lentoasema lisätty.")

        elif valinta == "2":
            icao = input("Anna haettava ICAO-koodi: ").strip().upper()
            if icao in lentoasemat:
                print(f"Lentoasema: {lentoasemat[icao]}")
            else:
                print("Lentoasemaa ei löytynyt.")

        elif valinta == "3":
            print("Ohjelma lopetetaan.")
            break

        else:
            print("Virheellinen valinta, yritä uudelleen.")

lentoasema_tiedot()
