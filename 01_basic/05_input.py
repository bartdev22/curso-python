###
# 05 - Entrada de usuario (input()) - Versión simplificada
# La función input() permite obtener datos del usuario a través de la consola.
###

from os import system
if system("clear") != 0: system("cls")

# Para obtener datos del usuario se usa la función input()
# La función input() recibe un mensaje que se muestra al usuario
# y devuelve el valor introducido por el usuario
nombre = input("Hola, ¿cómo te llamas?\n")
print(f"Hola {nombre}, encantado de conocerte")

# Ten en cuenta que la función input() devuelve un string
# Así que si queremos obtener un número se debe convertir el string a un número
age = input("¿Cuántos años tienes?\n")
age = int(age)
print(f"Tienes {age} años")

# También se puede usar la función int() directamente en la función input()
age = int(input("¿Cuántos años tienes?\n"))
print(f"Tienes {age} años")
# Si el usuario introduce un valor no válido, se generará un error
# Por ejemplo, si el usuario introduce un texto en lugar de un número
# age = int(input("¿Cuántos años tienes?\n"))  # ❌ ValueError: invalid literal for int() with base 10: 'twenty'

# La función input() también puede devolver múltiples valores
# Para hacerlo, el usuario debe separar los valores con una coma
print("Obtener múltiples valores a la vez")
country, city = input("¿En qué país y ciudad vives?\n").split()

print(f"Vives en {country}, {city}")