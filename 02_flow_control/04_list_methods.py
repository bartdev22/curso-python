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

# Métodos para agregar elementos a una lista
# 1) Método append(): Agrega un elemento al final de la lista.
# Añadir un elemento al final
lista1 = ['a', 'b', 'c', '@', 'd']
lista1.append('e')  # Agrega un nuevo elemento
print(lista1)  # ['a', 'b', 'c', 'd', 'e']

# 2) Método insert(): Inserta un elemento en una posición específica.
lista1.insert(2, '@')  # Inserta '@' en la posición 2
print(lista1)  # ['a', 'b', '@', 'c', 'd', 'e']

# 3) Método extend(): Extiende la lista agregando todos los elementos de otra lista.
# Añadir varios elementos al final
lista1.extend(['😃', '😍'])  # Agrega varios elementos
print(lista1)  # ['a', 'b', '@', 'c', 'd', 'e', '😃', '😍']

# 4) Método simple con +=
lista1 += ['x', 'y']  # Agrega varios elementos
print(lista1)  # ['a', 'b', '@', 'c', 'd', 'e', '😃', '😍', 'x', 'y']

# Métodos para eliminar elementos de una lista
# 1) Método remove(): Elimina la primera aparición de un valor específico. Se usa el valor que se desea eliminar, no el indice
lista1.remove('@') # Elimina la primera aparición de '@'
print(lista1)  

# 2) Método pop(): Elimina y devuelve el elemento en una posición específica mediante su indice. Si no se especifica el índice, elimina y devuelve el último elemento.
lista1.pop(5)
print(lista1)
lista1.pop() # Elimina el ultimo elemento
print(lista1)

# 3) Método del: Elimina un elemento en una posición específica mediante su índice. PREFERIBLEMENTE USAR EL METODO POP

# 4) Eliminar un rango de elementos usando slicing con del
del lista1[1:3] # Elimina los elementos en los indices 1 y 2
print(lista1)

# 5) Para eliminar todos los elementos de una lista se usa el metodo clear()
lista1.clear()
print(lista1) # Imprime una lista vacia []

# Métodos para ordenar una lista
# 1) Método sort(): Ordena los elementos de la lista en orden ascendente (de menor a mayor o alfabéticamente o numéricamente).
lista3 = [5, 2, 9, 100, 5, 6]
lista3.sort() # Ordena la lista de menor a mayor
print(lista3) # Imprime [2, 5, 5, 6, 9, 100]
# Esta lista ordena la lista original, modificandola, por lo que al imprimirla se muestran los cambios realizados en la lista original

# 2) Método sorted(): Devuelve una nueva lista ordenada sin modificar la lista original. Crea una copia ordenada que se guarda dentro de otra variable, la cual si estara ordenada, mientras que la original se mantendra igual y seguira sin cambios estando desordenada
lista4 = [35, 11, 4, 1, 5, 9]
sorted_lista4 = sorted(lista4) # Crea una nueva lista ordenada que se guarda en la nueva variable
print(f"\n\nLista original: {lista4}\n")
print(f"Lista nueva ordenada: {sorted_lista4}\n")

# 3) Ordenar en orden descendente
lista3.sort(reverse=True) # Ordena la lista de mayor a menor
print(lista3) # Imprime [100, 9, 6, 5, 5, 2]

# 4) Ordenar una lista de cadenas alfabéticamente. Al ser case sensitive, las mayúsculas se ordenan antes que las minúsculas, y luego se ordenan las minusculas
lista5 = ['banana', 'apple', 'Apple', 'ban', 'Banana', 'ban']
lista5.sort() # Ordena la lista alfabéticamente
print(lista5) # Imprime ['Apple', 'Banana', 'apple', 'banana', 'ban']

# 5) Ordenar una lista de cadenas alfabéticamente sin importar mayúsculas o minúsculas
lista5.sort(key=str.lower) # Ordena la lista alfabéticamente sin importar mayúsculas o minúsculas, donde va a comparar las mayusculas junto a su equivalente en minusculas, y se limitara a ordenar toda la lista alfabeticamente

print(lista5) # Imprime ['apple', 'Apple', 'banana', 'Banana', 'ban']

# Métodos para contar elementos en una lista
print(lista5.count('ban')) # Imprime 2, que es la cantidad de veces que aparece 'ban' en la lista5

# Metodos para verificar si un elemento existe en una lista o no
print('apple' in lista5) # Imprime True, ya que 'apple' si existe en la lista5
print('orange' in lista5) # Imprime False, ya que 'orange' no