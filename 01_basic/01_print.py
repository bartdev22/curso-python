###
# 01 - print()
# El módulo print() es el módulo que nos permite imprimir en consola
###

# Podemos importar módulos de Python para usarlos en nuestros programas.
# En este caso, importamos el módulo "os" que nos da acceso a funciones
# relacionadas con el sistema operativo
from os import system

# system() nos permite ejecutar un comando en la terminal.
# En este caso, lo hacemos para limpiar la pantalla tanto
# en MacOS/Linux usando "clear" como en Windows con "cls"
if system("clear") != 0: system("cls")

print("Este es un ejemplo básico de cómo imprimir un texto en consola")

print('Esto también funciona con comillas simples')

# Puedes imprimir múltiples elementos separados por un espacio
print("Python", "es", "genial")

# El parámetro 'sep' permite definir cómo se separan los elementos impresos
print("Python", "es", "brutal", sep = "-")

# El parámetro 'end' define lo que se imprime al final de la línea
print("Esto se imprime", end = " ") # Aquí, el 'end' es un espacio
print("en una línea") 

print("Esto se imprime", end = "\n") # Aquí, el 'end' es un salto de línea (comportamiento por defecto)
print("en una nueva línea")

# También puedes imprimir múltiples líneas usando el carácter de nueva línea \n
print("Primera línea\nSegunda línea\nTercera línea")

# También se pueden imprimir números directamente
print(42)

# Ejemplo de cómo imprimir el símbolo de pulgadas (")
# Si usamos comillas dobles dentro de un string con comillas dobles, se produce un error:
# print("Esto es una "pulgada"")  # ❌ Esto generaría un error de sintaxis

# ✅ Solución 1: Usar comillas simples para encerrar la cadena
print('Esto es una "pulgada" dentro de un string con comillas simples')

# ✅ Solución 2: Usar el carácter de escape \ para incluir comillas dobles dentro de un string con comillas dobles
print("Esto es una \"pulgada\" dentro de un string con comillas dobles")

# ✅ Solución 3: Usar triple comillas para definir el string
print("""Esto es una "pulgada" dentro de un string con triple comillas""")