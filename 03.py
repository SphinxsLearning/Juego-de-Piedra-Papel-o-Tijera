''' Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.
*
**
***
****
*****
******
'''
h = abs(int(input("Ingrese un ńumero entero: ")))
a = 1

while a <= h:
    print("*" * a)
    a += 1