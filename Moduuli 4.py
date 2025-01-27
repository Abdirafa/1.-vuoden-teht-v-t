#Teht 1

luku = 1
while luku <= 1000:
    if luku % 3 == 0:
        print(luku)
    luku += 1

#Teht 2

values = [10, 5, 0, -1]

for inches in values:
    if inches < 0:
        print("Ohjelma lopetettu.")
        break
    centimeters = inches * 2.54
    print(f"{inches} tuumaa on {centimeters:.2f} senttimetriä.")


#Teht 3

values = [5, 10, -3, 42, 0]

if values:
    smallest = min(values)
    largest = max(values)
    print(f"Pienin luku: {smallest}")
    print(f"Suurin luku: {largest}")
else:
    print("Ei lukuja syötetty.")

#Teht 4


computer_number = 267
guesses = [797, 56, 267]

for guess in guesses:
    if guess < computer_number:
        print(f"{guess} on liian pieni arvaus.")
    elif guess > computer_number:
        print(f"{guess} on liian suuri arvaus.")
    else:
        print(f"{guess} on oikein!")
        break


#Teht 5

Username = "python"
password = "rules"
error_count = 0

while error_count < 5:
    entered_username = input("Anna käyttäjätunnus")
    entered_password = input("laita salasana")
    if entered_username == Username and entered_password == password:
        print("Tervetuloa")
    else:
        print("väärä käyttäjätunnus tai salasana")
        error_count += 1

if error_count == 5:
    print("pääsy estetty")


