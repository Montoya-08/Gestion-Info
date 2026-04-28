import numpy as np

"""a = np.array([1, 2, 3, 4, 5])

#Sumar 2 a todos los valores del arreglo
a = a + 2

#Calcular la suma de los elementos del arreglo
suma = np.sum(a)

##Calcular promedio del arreglo
promedio = np.mean(a)

print(a)
print(suma)
print(promedio)"""

#Enunciado: Crea una matriz de 3 filas y 3 columnas llena de unos y cambia todos los valores a 5, calcula el valor máximo de la matriz y calcula la suma total de los elementos

matriz = np.ones((3, 3))
matriz = matriz * 5
maximo = np.max(matriz)
suma_total = np.sum(matriz)

print(matriz)
print(maximo)
print(suma_total)