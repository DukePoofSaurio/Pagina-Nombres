import numpy as np

arreglo1 = np.array([2, 4, 6, 8, 10])
arreglo4 = np.array([1, 3, 5, 7, 9])

arreglo2 = np.ones((4, 4))

arreglo3 = np.zeros((2, 2, 2))

for x in arreglo1:
    print(x)

maximo = np.max(arreglo1)
minimo = np.min(arreglo1)
media = np.mean(arreglo1)
posmax = np.argmax(arreglo1)
posmin = np.argmin(arreglo1)

print("Valor Mayor = ", maximo)
print("Valor Menor = ", minimo)
print("Media = ", media)
print("Posmax = ", posmax)
print("Posmin = ", posmin)

arreglo6 = np.sum(arreglo1 + arreglo4)

print("Suma de Arreglos = ", arreglo6)

##print("Valor Mayor = ", np.max(arreglo1))
##print("Valor Menor = ", np.min(arreglo1))

##for y in arreglo2:
    ##print(y)

##for y in arreglo3:
    ##print(y)
