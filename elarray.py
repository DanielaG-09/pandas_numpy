## Importar librerias
import numpy as np

## Crear lista
lista = [1,2,3,4,5,6,7,8,9]
print(lista)

## Llevar el array a numpy
np.array(lista) # verificar si se escribe o no
arr = np.array(lista)
print(arr)

## Verificar el tipo de objeto
print(type(arr))

## Crear una matriz
matriz = [[1,2,3],[4,5,6],[7,8,9]]
matriz = np.array(matriz)
print(matriz)

## Aplicar indexin
print(arr[1])
print(arr[0]+arr[5])
print(matriz)
print(matriz[0])

## Imprimir filas
print(matriz[1])
print(matriz[2])
#print(matriz[3]) #No existe fila 3

#Imprimir columnas
print(matriz[0,2])

## Seleccionar de puntos especificos
print(arr[:6])
print(arr[2:])
print(arr[:])

## Seleccionar por pasos
print(arr[::3]) #quiero todo de tres en tres
print(arr[-1]) #ver el último valor con -1
print(arr[-3:]) #ver los últimos tres valores

## Slice con matriz
print(matriz[1:]) #el primer valor haría referencia a la fila 1
print(matriz[1:,0:2]) #columnas de la 0 a la 2