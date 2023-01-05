import numpy as np
import random
##Ejercicio 1
## hacer las operaciones con matrices cuadradas"

A = []
B = []


def suma_nump():
    suma = np.array(A)+np.array(B)

    print("Esta es la suma de las matrices ")
    print(suma)


def resta_nump():
    resta = np.array(A)-np.array(B)
    print("Resta de matrices ")
    print(resta)


def multiplicacion():
    multi = np.dot(A, B)
    print("Este es la multiplicacion de las matrices")
    print(multi)


def pedir_f():
    filas = int(input("Digame la cantidad de filas:"))
    return filas


def pedir_c():
    columnas = int(input("Digame la cantidad de columnas: "))
    return columnas


def llenar(matriz):
    filas = pedir_f()
    columnas = pedir_c()
    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            matriz[i].append(random.randint(1, 10))
    print(matriz)

llenar(A)
llenar(B)
suma_nump()
resta_nump()
multiplicacion()


