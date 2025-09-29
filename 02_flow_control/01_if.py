print("Estos son los flujos de control, condicionales y demas")

# Format if

age = 18
if age >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

if age == 18:
    print("En caso de tabular mas de una linea")
    print("Se recomienda usar llaves para encerrar el bloque, pero en python no es necesario, se usa la indentacion")

# Format elif
if age > 18:
    print("Eres mayor de edad")
elif age == 18:
    print("Tienes 18 años")
else:
    print("Eres menor de edad")


# Ejemplo de Anidacion (Evitarlo)
edad = 20
tiene_dinero = True
 
if edad >= 18:
   if tiene_dinero:
      print("Puedes ir a la discoteca")
   else:
      print("Quédate en casa")
else:
    print("No puedes entrar a la disco")

# Mismo ejemplo sin anidacion (Preferible)

if edad < 18:
    print("No puedes entrar a la disco")
elif tiene_dinero:
    print("Puedes ir a la discoteca")
else:
    print("Quédate en casa")

# Condiciones ternarias con if-else
# Formato:
# [valor_si_verdadero] if [condición] else [valor_si_falso]

print("La condición ternaria:")
edad = 17
mensaje = "Es mayor de edad"

print(mensaje) if edad >= 18 else print("Es menor de edad")