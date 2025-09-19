# Operadores Logicos en Python
# and, or, not

age = 20
has_money = True

if age >= 18 and has_money:
    print("Puedes ir a la discoteca")

if age >= 18 or has_money:
    print("Puedes ir a la discoteca")

if not has_money:
    print("No tienes dinero")   

# Booleanos
print(5 > 3)    # True
print(5 < 3)    # False
print(5 == 5)   # True
print(5 != 3)   # True
print(5 >= 5)   # True
print(5 <= 3)   # False
# Si se comparan dos strings, tiene case sensitive

# Tabla de verdad and
"""
# A     B     A and B
# True  True   True
# True  False  False
# False True   False
# False False  False
"""

# Tabla de verdad or
"""
# A     B     A or B
# True  True   True
# True  False  True
# False True   True
# False False  False
"""

# Tabla de verdad not
"""
# A     not A
# True   False
# False  True
"""

# Otros tipos de valores bool serian los numeros distintos a 0 == True y 0 == False. Y en el caso de los strings seria cualquier string no vacio == True y el string vacio "" == False.

# Ejemplo int
numero = 5
if numero: # True
   print("El número no es cero")
 
numero = 0
if numero: # False
   print("Aquí no entrará nunca")

# Ejemplo string

nombre = "Juan"
if nombre:
   print("El nombre no es vacío")
 
nombre = ""
if nombre:
    print("El nombre no es vacío") # Aquí no entrará nunca

# La estructura del if es sencillamente usar la condicion y la sentencia. La condicion se está evaluando como True, donde si el valor condicionado es True, se ejecuta la sentencia. Si es False, no se ejecuta nada, o en consecuencia se ejecutaria un else o un elif.