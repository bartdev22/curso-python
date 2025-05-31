###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

from os import system
if system("clear") != 0: system("cls")

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad.\n")

# Solución ejercicio 1.

nombre, ciudad = input("Hola! Indicame tu nombre y de que ciudad provienes.\n").split()
print(f"Genial! un saludo {nombre}, algun dia quiero visitar {ciudad}\n\n")

print("--------------")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

### Solucion ejercicio 2

print("Las siguientes variables son de los siguientes tipos")
print(f"La variable 'a', la cual tiene un valor de {a}, es de tipo {type(a)}")
print(f"La variable 'b', la cual tiene un valor de {b}, es de tipo {type(b)}")
print(f"La variable 'c', la cual tiene guardado '{c}', es de tipo {type(c)}")
print(f"La variable 'd', la cual tiene el valor de {d}, es de tipo {type(d)}")
print(f"La variable 'e', la cual no tiene un valor guardado, es de tipo {type(e)}")


print("--------------")

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

### Completa aquí
prueba3 = "12345"
print(f"El tipo de dato de la variable prueba3 es: {type(prueba3)}")
prueba3 = int(prueba3)
print(f"El tipo de dato de la variable prueba3 es: {type(prueba3)}")
prueba3 = float(prueba3)
print(f"El tipo de dato de la variable prueba3 es: {type(prueba3)}")

prueba3 = 3.99
prueba3 = int(prueba3)
print(f"La variable 'prueba3' ahora es de tipo {type(prueba3)} y su valor es {prueba3}")


print("--------------")

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

# Solución ejercicio 4
nombre = "bart"
edad = 23
altura = 1.77
print(f"Esta es la prueba 4. Mi nombre es {nombre}, tengo {edad} a;os de edad y mido {altura} metros.\n")


print("--------------")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")

pi = int(round(3.14) / 2)  # Redondea el número PI
print(f"El resultado de dividir pi (3.14) entre 2 es: {pi}")