#Teht 1

num = 1

while num <= 1000:
    if num % 3 == 0:
        print(num)
    num += 1

#Teht 2

while True:
    inches = float(input("tuumamäärä (lopet negatiivise): "))
    if inches < 0:
        break
    cm = inches * 2.54
    print(f"{inches} tuumaa on {cm:.2f} cm")

#Teht 3

numbers = []

while True:
    user_input = input("Anna luku : ")
    if user_input == "":
        break
    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("Virheellinen syöte, anna numero.")

if numbers:
    print(f"Pienin luku: {min(numbers)}")
    print(f"Suurin luku: {max(numbers)}")
else:
    print("Eiantanut yhtään lukua.")

#Teht 4

import random

salainen_luku = random.randint(1, 10)

while True:
    try:
        arvaus = int(input("Arvaa luku väliltä 1-10: "))
        if arvaus < salainen_luku:
            print("Liian pieni arvaus")
        elif arvaus > salainen_luku:
            print("Liian suuri arvaus")
        else:
            print("Oikein!")
            break
    except ValueError:
        print("Anna kokonaisluku väliltä 1-10.")

#Teht 5

MAX_YRITYKSET = 5
OIKAIS_TUNNUS = "python"
OIKEA_SALASANA = "rules"

yritykset = 0

while yritykset < MAX_YRITYKSET:
    kayttajatunnus = input("Anna käyttäjätunnus: ")
    salasana = input("Anna salasana: ")

    if kayttajatunnus == OIKAIS_TUNNUS and salasana == OIKEA_SALASANA:
        print("Tervetuloa")
        break
    else:
        print("Väärä tunnus tai salasana.")
        yritykset += 1

if yritykset == MAX_YRITYKSET:
    print("Pääsy evätty.")


