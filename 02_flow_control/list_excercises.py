###
# EJERCICIOS DE LISTAS
###

# Ejercicio 1: El mensaje secreto
# Dada la siguiente lista:
# mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
# Utilizando slicing y concatenación, crea una nueva lista que contenga solo el mensaje "secreto".
print("Ejercicio 2: Mensaje Secreto \n")
mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
lista_secreto = mensaje[7:]
print(lista_secreto)  # Imprime ['s', 'e', 'c', 'r', 'e', 't', 'o']

# Ejercicio 2: Intercambio de posiciones
# Dada la siguiente lista:
# numeros = [10, 20, 30, 40, 50]
# Intercambia la primera y la última posición utilizando solo asignación por índice.
print("\nEjercicio 2: Intercambio de posiciones en una lista \n")
numeros_intercambio = [10, 20, 30, 40, 50]
print("Lista original:", numeros_intercambio)
#Intercambio de doble asignacion en una misma linea / una sola sentencia
numeros_intercambio[0], numeros_intercambio[-1] = numeros_intercambio[-1], numeros_intercambio[0]
print("Lista después del intercambio:", numeros_intercambio)

# Ejercicio 3: El sándwich de listas
# Dadas las siguientes listas:
# pan = ["pan arriba"]
# ingredientes = ["jamón", "queso", "tomate"]
# pan_abajo = ["pan abajo"]
# Crea una lista llamada sandwich que contenga el pan de arriba, los ingredientes y el pan de abajo, en ese orden.
print("Ejercicio 3: El sándwich de listas \n")
pan = ["pan arriba"]
ingredientes = ["jamón", "queso", "tomate"]
pan_abajo = ["pan abajo"]
sandwich = pan + ingredientes + pan_abajo
print("La lista 'sandwich' Esta conformada por: ",sandwich) 


# Ejercicio 4: Duplicando la lista
# Dada una lista:
# lista = [1, 2, 3]
# Crea una nueva lista que contenga los elementos de la lista original duplicados.
# Ejemplo: [1, 2, 3] -> [1, 2, 3, 1, 2, 3]
print("\nEjercicio 4: Duplicando la lista \n")
lista = [1, 2, 3]
print("Lista original: ", lista)
lista = lista * 2
print("Lista duplicada: ", lista)

# Ejercicio 5: Extrayendo el centro
# Dada una lista con un número impar de elementos, extrae el elemento que se encuentra en el centro de la lista utilizando slicing.
# Ejemplo: lista = [10, 20, 30, 40, 50] -> El centro es 30
print("\nEjercicio 5: Extrayendo el centro de una lista\n")
lista_centro = [10, 20, 30, 40, 50]
centro = len(lista_centro) // 2 # 5/2 = 2.5 -> 2, 2 es el indice del centro de la lista
print("El elemento central de la lista es: ", lista_centro[centro]) # Imprime 30

# Ejercicio 6: Reversa parcial
# Dada una lista, invierte solo la primera mitad de la lista (utilizando slicing y concatenación).
# Ejemplo: lista = [1, 2, 3, 4, 5, 6] -> Resultado: [3, 2, 1, 4, 5, 6]
print("\nEjercicio 6: Reversion parcial de una lista \n")
lista_inversa = [1, 2, 3, 4, 5, 6]
mitad = len(lista_inversa) // 2
lista_inversa = lista_inversa[:mitad][::-1] + lista_inversa[mitad:]
print("Resultado de la Lista con la primera mitad invertida: ", lista_inversa)  #