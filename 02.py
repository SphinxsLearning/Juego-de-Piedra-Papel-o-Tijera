""" Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas. """
num = int(input("Ingrese un número entero positivo: "))
a = 1

while a <= num:
    if a == 1:
        print(a)
        a += 1
    elif (a % 2) != 0:
        print(a)
        a += 1
    else:
        a += 1