###
# 03 - casting de types
# Transformar un tipo de un valor a otro
###

from os import system
if system("clear") != 0: system("cls")

print("Conversión de tipos")

# Convertir una cadena que contiene un número a un entero y sumarlo con otro entero
print(2 + int("100"))  # Convierte "100" a entero y suma 2. Resultado: 102

# Convertir un entero a cadena para concatenarlo con otra cadena
print("100" + str(2))  # Convierte el número 2 a cadena y lo concatena. Resultado: "1002"

# Convertir una cadena con un número decimal a tipo float
print(type(float("3.1416")))  # Convierte "3.1416" a float y muestra su tipo. Resultado: <class 'float'>

# Convertir un número decimal a entero (se trunca la parte decimal)
print(int(3.1416))  # Convierte 3.1416 a 3 eliminando la parte decimal. Resultado: 3
print(int(3.9999))  # También convierte 3.9999 a 3. Resultado: 3. Nunca se redondea, ya que un casting no realiza operaciones matemáticas.

# Evaluar valores numéricos como booleanos
print(bool(3))  # Cualquier número distinto de 0 es True. Resultado: True
print(bool(0))  # 0 es False. Resultado: False
print(bool(-1))  # Números negativos también son True. Resultado: True

# Evaluar cadenas como booleanos
print(bool(""))  # Una cadena vacía es False. Resultado: False
print(bool(" "))  # Una cadena con espacios es True. Resultado: True
print(bool("False"))  # Una cadena con texto, aunque sea "False", es True. Resultado: True

# Redondear un número decimal
print(round(2.49))  # Redondea 2.49 al entero más cercano. Resultado: 2
print(round(2.5))  # Cuando el redondeo se hace con un .5, se redondea al entero par más cercano. Resultado: 2
print(round(2.51))  # Redondea 2.51 al entero más cercano. Resultado: 3

# Este genera un error y se comenta para evitar conflicto en la ejecución
# No se puede convertir una cadena que no representa un número a un entero. Generará un ValueError.
# print(int("Hola mundo"))  # ❌ Esto generaría un ValueError porque "Hola mundo" no es un número