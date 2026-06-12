from random import randint

numin = int(input("Ingrese la cantidad de datos que va a ingresar: "))
arreglo = [randint(0,9) for _ in range(numin)]

print("Este es el vector original:")
print(*arreglo, sep='\n')

for i in range(numin):
    minimo = i
    for j in range(i,numin):
        if arreglo[j] < arreglo[minimo]:
            minimo = j
    arreglo[i], arreglo[minimo] = arreglo[minimo], arreglo[i]

print("Este es el vector ordenado:")
print(*arreglo, sep='\n')
