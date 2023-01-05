## Ejercicio 1 - Arreglos
A = int(input(u"Ingrese el tamaño de los arreglos: "))
B = []
C = []
for i in range (0,A):
  B.append(input("Ingrese nombre de las personas: "))
print(B) 
for j in range (0,A):
  C.append(len(B[j]))
print(C) 

## Ejercicio 2 - Arreglos
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

##Ejercicio  3 - Arreglos
A = int(input("Ingrese el tamaño del arreglo: "))
B = int(input("Ingrese el número de múltiplos: "))
C = []
for i in range(0,A):
    C.append((i+1)*B)
print(C)

##Ejercicio 4 - Arreglos
