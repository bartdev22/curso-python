"""
Ejercicios prácticos
Ejercicio 1: Determinar el mayor de dos números

Pide al usuario que introduzca dos números y muestra un mensaje indicando cuál es mayor o si son iguales.
"""
numero1 = int(input("Indique el primer numero: "))
numero2 = int(input("Indique el segundo numero: "))
print(f"El mayor es: {max(numero1, numero2)}") if numero1 != numero2 else "Son iguales"

"""
Ejercicio 2: Calculadora simple

Pide al usuario dos números y una operación (+, -, *, /). Realiza la operación y muestra el resultado (maneja la división entre cero).
"""
numero1 = int(input("Indique el primer numero: "))
numero2 = int(input("Indique el segundo numero: "))
operacion = input("Indique la operación (+, -, *, /): ")

if operacion not in ["+","-","*","/"]:
    print("Operación no válida")
elif operacion == "+":
    print(f"El resultado de la suma es: {numero1 + numero2}")
elif operacion == "-":
    print(f"El resultado de la resta es: {numero1 - numero2}")
elif operacion == "*":
    print(f"El resultado de la multiplicación es: {numero1 * numero2}")
elif operacion == "/":
    if numero2 == 0:
        print("Error: División entre cero no permitida")
    else:
        print(f"El resultado de la división es: {numero1 / numero2}")
"""
Ejercicio 3: Año bisiesto

Pide al usuario que introduzca un año y determina si es bisiesto:

Es divisible por 4.
Excepto si es divisible por 100, pero no por 400.
"""
año = int(input("Indique un año: "))
if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print(f"El año {año} es bisiesto")
else:
    print(f"El año {año} no es bisiesto")

"""
Ejercicio 4: Categorizar edades

Clasifica una edad ingresada por el usuario en:

Bebé (0-2 años)
Niño (3-12 años)
Adolescente (13-17 años)
Adulto (18-64 años)
Adulto mayor (65 años o más)
"""
edad = int(input("Indique su edad: "))
if edad < 0:
    print("Edad no válida")
elif edad <= 2:
    print("Bebé")
elif edad <= 12:
    print("Niño")
elif edad <= 17:
    print("Adolescente")
elif edad <= 64:
    print("Adulto")
else:
    print("Adulto mayor")