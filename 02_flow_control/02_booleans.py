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