import random

""" Realiza un programa que simule el juego de piedra, papel o tijera. Una partida de 2 de 3 rondas. """

print("-" * 26)
print("| PIEDRA, PAPEL o TIJERA |")
print("-" * 26)

número_de_ronda = 1
your_number_wins = 0
pc_number_wins = 0

pc_options = ("piedra", "papel", "tijera")

while your_number_wins < 2 and pc_number_wins < 2:
    print()
    print("RONDA", número_de_ronda)
    you = input("Elije: Piedra, Papel o Tijera: ").lower()
    if not you in pc_options:
        continue
    pc = random.choice(pc_options)

    if you == pc:
        print(f"Elegiste: {you.capitalize()}, PC eligio: {pc.capitalize()} -> EMPATE  ")
    elif you == "piedra":
        if pc == "papel":
            print(f"Elegiste: {you.capitalize()}, PC eligio: {pc.capitalize()} -> PC GANA")
            pc_number_wins += 1
        else:
            print(f"Elegiste: {you.capitalize()}, PC eligio: {pc.capitalize()} -> GANASTE")
            your_number_wins += 1
    elif you == "papel":
        if pc == "piedra":
            print(f"Elegiste: {you.capitalize()}, PC eligio: {pc.capitalize()} -> GANASTE")
            your_number_wins += 1
        else:
            print(f"Elegiste: {you.capitalize()}, PC eligio: {pc.capitalize()} -> PC GANA")
            pc_number_wins += 1
    elif you == "tijera":
        if pc == "piedra":
            print(f"Elegiste: {you.capitalize()}, PC eligio: {pc.capitalize()} -> PC GANA")
            pc_number_wins += 1
        else:
            print(f"Elegiste: {you.capitalize()}, PC eligio: {pc.capitalize()} -> GANASTE")
            your_number_wins += 1
    número_de_ronda += 1

print()
if your_number_wins > pc_number_wins:
    print('*' * 22)
    print('* EL GANADOR ES USER *')
    print('*' * 22)
else:
    print('*' * 32)
    print('* EL GANADOR ES PC MASTER RACE *')
    print('*' * 32)