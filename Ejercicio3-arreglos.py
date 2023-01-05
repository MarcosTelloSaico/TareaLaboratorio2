A = int(input("Ingrese el tamaño del arreglo: "))
B = int(input("Ingrese el número de múltiplos: "))
C = []
for i in range(0,A):
    C.append((i+1)*B)
print(C)
