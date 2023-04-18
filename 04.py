''' Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.
1
3 1
5 3 1
7 5 3 1
9 7 5 3 1
'''
h = abs(int(input("Ingrese un número entero: ")))
a = 1

while a <= h:
    if a == 1:
        print(a)
        a += 2
    else:
        b = a
        while b > 1:
            print(b)
            b -= 2