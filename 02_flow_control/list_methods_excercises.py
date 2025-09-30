"""
Ejercicio 1: Añadir y modificar elementos
    Crea una lista con los números del 1 al 5.
    Añade el número 6 al final usando append().
    Inserta el número 10 en la posición 2 usando insert().
    Modifica el primer elemento de la lista para que sea 0.
"""
list1 = [1, 2, 3, 4, 5]
list1.append(6)
list1.insert(2,10)
list1[0] = 0
print(f"\nLa lista 1 del primer ejercicio es: {list1}\n")

"""
Ejercicio 2: Combinar y limpiar listas
    Crea dos listas:
    lista_a = [1, 2, 3]
    lista_b = [4, 5, 6, 1, 2]
    Extiende lista_a con lista_b usando extend().
    Elimina la primera aparición del número 1 en lista_a usando remove().
    Elimina el elemento en el índice 3 de lista_a usando pop() e imprime el elemento eliminado.
    Limpia completamente lista_b usando clear().
"""
list_a = [1,2,3]
list_b = [4,5,6,1,2]
list_a.extend(list_b)
list_a.remove(1)
list_a.pop(3)
print(f"La lista final del ejercicio 2 es: {list_a}\n")
list_a.clear()
print(f"La lista luego de vaciarla es: {list_a}")

"""
Ejercicio 3: Slicing y eliminación con del
    Crea una lista con los números del 1 al 10.
    Usa slicing y del para eliminar los elementos desde el índice 2 hasta el 5 (sin incluir el 5).
    Imprime la lista resultante.
"""
list_3 = [1,2,3,4,5,6,7,8,9,10]
del list_3[2:5]
print(f"La lista 3 luego de eliminar con del slicing es: {list_3}")

"""
Ejercicio 4: Ordenar y contar
    Crea una lista con los siguientes números: [5, 2, 8, 1, 9, 4, 2].
    Ordena la lista de forma ascendente usando sort().
    Cuenta cuántas veces aparece el número 2 en la lista usando count().
    Comprueba si el número 7 está en la lista usando in.
"""
list_4 = [5,2,8,1,9,4,2]
list_4.sort()
print(f"La lista 4 ordenada es: {list_4}")
print(f"El numero '2' aparece : {list_4.count(2)} veces en la lista")

"""
Ejercicio 5: Copia vs. Referencia
    Crea una lista llamada original con los números [1, 2, 3].
    Crea una copia de la lista original llamada copia_1 usando slicing.
    Crea otra copia llamada copia_2 usando copy().
    Crea una referencia a la lista original llamada referencia.
    Modifica el primer elemento de la lista referencia a 10.
    Imprime las cuatro listas (original, copia_1, copia_2, referencia) y observa los cambios.
"""
main_list = [1,2,3]


"""
Ejercicio 6: Ordenar strings sin diferenciar mayúsculas y minúsculas
    Crea una lista con las siguientes cadenas: ["Manzana", "pera", "BANANA", "naranja"].
    Ordena la lista sin diferenciar entre mayúsculas y minúsculas.
"""
list_strings = ["Manzana", "pera", "BANANA", "naranja"]
list_strings.sort(key=str.lower)
print(f"La lista string ordenada es: {list_strings}")