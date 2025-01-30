#Teht 1

import random
def heita_noppaa():
    heitot = [3, 2, 5, 1, 4, 6]
    return heitot.pop(0)
print("Heitetään noppaa, kunnes saadaan kuutonen:")
while (silmaluku := heita_noppaa()) != 6:
    print(silmaluku)
print(6)

#Teht 2

import random

def heita_noppaa_tahkoilla(tahkot):
    heitot = list(range(1, tahkot + 1))
    return heitot.pop(0)
max_silmaluku = int(input("Anna nopan tahkojen määrä: "))
print(f"Heitetään {max_silmaluku}-tahoista noppaa, kunnes saadaan maksimi:")
while (silmaluku := heita_noppaa_tahkoilla(max_silmaluku)) != max_silmaluku:
    print(silmaluku)
print(max_silmaluku)

#Teht3

def gallonat_litroiksi(gallonat):
    return gallonat * 3.785

while True:
    gallonat = float(input("Anna bensiinimäärä gallonoina (negatiivinen lopettaa): "))
    if gallonat < 0:
        break
    print(f"Vastaava litramäärä: {gallonat_litroiksi(gallonat):.2f} LL")