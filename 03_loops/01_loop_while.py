# Bucle con una simple condición
contador = 0
 
print("\nPrimer bucle while:\n")
while contador <= 5:
   print(contador)
   contador += 1  # Es importante incrementar para evitar un bucle infinito
else: print("El bucle ha terminado (esto se imprime con el else)")

# Break en Bucles
print("\nSegundo bucle while usando break:\n")
while True:
   print(contador)
   contador += 1
   if contador == 15:
      break # Sale del bucle
   
# Continue en Bucles
print("\nTercer bucle while usando continue:\n")
contador = 0
 
while contador < 10:
   contador += 1
 
   if contador % 2 == 0:
       continue  # Salta los números pares
 #Este continue si se cumple ignora absolutamente todo el codigo que le siga en este bloque
   print(contador)

# Ejercicios con el Ciclo While
# 1) Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.
conteo_regresivo = 12
while conteo_regresivo > 1:
    conteo_regresivo -= 1
    if conteo_regresivo >=1 and conteo_regresivo<=10:
       print(conteo_regresivo)

# Ejercicio 2: Suma de números pares
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.
num = 1
num_sum = 0
while num <= 20:
   num+=1
   if num % 2 == 0:
      num_sum = num + num_sum
      print(f"La suma actual es: {num_sum}")

# Ejercicio 3: Factorial de un número
# Pide al usuario un número entero positivo y calcula su factorial.

num_factorial = int(input("Indique el numero que desea saber el factorial: \n"))
factorial = num_factorial
while factorial > 1:
   factorial -= 1
   num_factorial += factorial
   if factorial == 1:
      print(f"El factorial es: {num_factorial}")

# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña que debe tener al menos 8 caracteres.

password = input("Indique su contrasena: ")
while len(password) < 8:
   print("La contrasena debe ser de minimo 8 caracteres\n Indique nuevamente la contrasena:")
   password = input("Indique su contrasena: ")
else: print(f"Su contrasena es: {password}")

# Ejercicio 5: Tabla de multiplicar
# Pide al usuario un número e imprime su tabla de multiplicar del 1 al 10.

numero = int(input("Introduce un número: "))
multiplicador = 1

while multiplicador <= 10:
  resultado = numero * multiplicador
  print(f"{numero} x {multiplicador} = {resultado}")
  multiplicador += 1

# Ejercicio 6: Numeros primos hasta N
# Pide al usuario un número entero positivo N e imprime todos los números primos hasta N.
n = int(input("Introduce un número entero positivo N: "))

numero = 2 
while numero <= n:
  es_primo = True  # Asumimos que el número es primo hasta que se demuestre lo contrario
  divisor = 2
  while divisor * divisor <= numero:  # Optimizamos: no es necesario probar divisores hasta numero
    if numero % divisor == 0:
      es_primo = False  # Si encontramos un divisor, no es primo
      break  # Salimos del bucle interior
    
    divisor += 1

  if es_primo:
    print(numero)

  numero += 1