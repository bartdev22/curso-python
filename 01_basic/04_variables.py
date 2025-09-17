"""
    Las variables en Python son de tipado dinámico, es decir el tipo de dato se determina en tiempo de ejecución. No hace falta declararlo directamente. Si uso una variable que contenga un int, luego le puedo guardar un valor string sin problema.
"""

x = 5
print(x)
print(type(x))

x = "texto"
print(x)
print(type(x))

# Constantes. Se declaran en mayúsculas, pero no son realmente constantes, es solo una convención.
PI = 3.1416

# Ese valor de constante sigue siendo una variable, se puede cambiar el valor; en Python no hay constantes reales, por lo tanto se declaran en mayúsculas para indicar que no deberían cambiarse.

# f-strings: forma de formatear strings en Python 3.

nombre = "Juan"
edad = 30
print(f"Él es {nombre} y tiene {edad} años.")
#Se usan variables, y dentro del string se inicia con un f para declarar que es un format string. Sumado a esto las variables que se vayan a agregar en el print van entre llaves {}.

# Declaraciones de variables. Convenciones
mi_variable = 10          # snake_case RECOMENDADO
miVariable = 20          # camelCase
MiVariable = 30          # PascalCase
mi_variable_con_numeros2 = 40  # con números
#mi-variable-con-guiones = 50  # no se puede usar guiones en nombres de variables

# Por último, no se pueden usar palabras reservadas del lenguaje como nombres de variables. (print, if, else, for, while, etc)