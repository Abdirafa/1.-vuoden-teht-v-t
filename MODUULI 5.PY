#Teht1

import random

n = 3
summa = 0

for _ in range(n):
    heitto = random.randint(1, 6)
    print(f"Heitto: {heitto}")
    summa += heitto

print(f"Heittojen summa: {summa}")

#Teht 2

numbers = [12, 45, 78, 23, 89, 56, 90, 34, 67, 100]

numbers.sort(reverse=True)

print("Viisi suurinta lukua:", numbers[:5])

#Teht 3

def onko_alkuluku(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

luvut = [10, 13, 17, 21, 29, 33]

for luku in luvut:
    if onko_alkuluku(luku):
        print(f"{luku} on alkuluku.")
    else:
        print(f"{luku} ei ole alkuluku.")

#Teht 4

kaupungit = ["Pariisi", "Lontoo", "Rooma", "Berliini", "Madrid"]

print("\nSyöttämäsi kaupungit:")
for kaupunki in kaupungit:
    print(kaupunki)

