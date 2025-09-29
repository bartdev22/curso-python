import os
os.system("clear")
"""
Las listas en python, son como los arrays en otros lenguajes, con la diferencia de que se pueden almacenar datos hetergeneos, es decir, se pueden tener distintos tipos de datos en una misma lista. Funcionan igual que los arrays, donde si sumas dos listas, estas se concatenan.

Para crear una lista, se utilizan corchetes [] y los elementos se separan por comas. Por ejemplo: mi_lista = [1, 2, 3, "hola", True].

Para saber la longitud de una lista, se utiliza la función len(). Por ejemplo: len(mi_lista) nos devolverá 5.
"""

# Creación de listas
lista1 = [1, 2, 3, 4, 5]  # Lista de enteros
lista2 = ["manzanas", "peras", "plátanos"]  # Lista de cadenas
lista3 = [1, "hola", 3.14, True]  # Lista de tipos mixtos
 
# Otras formas de listas
lista_vacia = []  # Lista vacía
lista_de_listas = [[1, 2], ["calcetin", 4]]  # Lista de listas
matrix = [[1, 2], [2, 3], [4, 5]]  # Lista que representa una matriz
# La lista matrix tiene 3 filas y 2 columnas, se verias asi:
# 1 2
# 2 3
# 4 5

# Acceso a elementos de una lista mediante su indice. Comenzando por el primer elemento en el indice 0.
# Se puede acceder al ultimo elemento con el indice -1, al penultimo con -2, y asi sucesivamente.
print(lista1[0])  # Imprime 1
print(lista2[1])  # Imprime "peras"
print(lista3[-1])  # Imprime True

# En una lista de listas, se accede primero a la lista externa y luego a la interna.
print(lista_de_listas[0][1])  # Imprime 2

# Print de listas con sus estructuras
print(lista1)  # Imprime [1, 2, 3, 4, 5]
print(lista2)  # Imprime ['manzanas', 'peras', 'plátanos']
print(lista3)  # Imprime [1, 'hola', 3.14, True]
print(lista_vacia)  # Imprime []
print(lista_de_listas)  # Imprime [[1, 2], ['calcetin', 4]]
print(matrix)  # Imprime [[1, 2], [2, 3], [4, 5]]

# Modificar un elemento
lista1[0] = 20  # Cambia el primer elemento
print(lista1)  # [20, 2, 3, 4, 5]

#Añadir elementos a una la lista
lista1 += [6, 7]  # Añade 6 y 7 al final de la lista