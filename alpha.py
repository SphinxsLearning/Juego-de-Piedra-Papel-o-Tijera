""" Realiza un programa que dado un número entero lo invierta. """
n = int(input("Ingresa un número entero: "))
a = n
inv = 0

while a > 0:
    if a < 10:
        inv = 10 * inv + a
        a = 0
    else:
        inv = 10 * inv + (a % 10)
        a = a // 10

print(f"{n} invertido es: {inv}")