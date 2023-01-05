A = [20, 15, 12, 11, 8, 4, 1]
alto = 20
bajo = alto
for i in A:
    if i < bajo:
        bajo = i
print("El promedio más bajo es: ",bajo)
A.remove(bajo)
print("La nota más baja, fué eliminada",A)
suma = 0
for j in A:
    suma += j
print("El promedio de las notas sobrantes es: ",suma/len(A))