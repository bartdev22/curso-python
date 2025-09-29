# En python a pesar de que es un lenguaje de tipado dinámico, se pueden hacer ciertas especificaciones/aclaraciones al código con anotaciones de type hints. Esto no es de que hace que una variable sea unicamente de ese tipo, no se puede porque python es de tipado dinámico, pero si que sirve para aclarar el tipo de dato que se espera en esa variable, función, etc. Esto es útil para mejorar la legibilidad del código y para herramientas de análisis estático de código.

# Ejemplo de type hints con verificacion de usuario en login

is_user_logged_in: bool = True
username: str = "admin"
password: str = "password123"
login_attempts: int = 3

# Funciones input

nombre = input ("Ingrese su nombre: ")  
print(f"Hola, {nombre}!")

país, ciudad = input("De qué país y ciudad eres? ").split()
print(f"Eres de {ciudad}, {país}")

edad = int(input("Cuantos años tienes? "))
print(f"Tienes {edad} años! El próximo año tendrás {edad + 1} años")