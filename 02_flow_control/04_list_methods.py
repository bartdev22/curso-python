# Slicing de listas 
import os
os.system("clear")
# Lista original
lista1 = [1, 2, 3, 4, 5]
 
# Slicing de la lista
print(lista1[1:4])  # Sublista desde el índice 1 hasta el índice 4 (sin incluir el índice 4): [2, 3, 4]
print(lista1[:3])   # Sublista desde el inicio hasta el índice 3 (sin incluirlo): [1, 2, 3]
print(lista1[3:])   # Sublista desde el índice 3 hasta el final: [4, 5]
print(lista1[:])    # Copia completa de la lista: [1, 2, 3, 4, 5]
 
# Soluciones
# 1 -> [2, 3, 4]
# 2 -> [1, 2, 3]
# 3 -> [4, 5]
# 4 -> [1, 2, 3, 4, 5]

# En python ademas de poder acceder a las listas, y además de poder acceder a ciertos elementos de esta mediante el slicing, se puede acceder a ciertos elementos de manera salteada usando el tercer parametro del slicing, que es el step o paso.
# Indices pares: Se va a acceder a los elementos de INDICES pares, salteandose a los demás

lista2 = [1,2,3,4,5,6,7,8,9,10]
print(lista2[::2]) # Imprime [1, 3, 5, 7, 9] que son los indices pares (0, 2, 4, 6, 8)

# Tambien se puede acceder con el step a modo negativo, es decir, se accede a la lista de manera inversa, empezando por el ultimo elemento y terminando en el primero.
print(lista2[::-1]) # Imprime [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] que es la lista al reves

# Como saber la longitud de una lista. Se usa la funcion len()
print("La longitud de la lista 2 es: ", len(lista2))