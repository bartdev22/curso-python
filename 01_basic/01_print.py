###
# 01 - print()
# print() allows the printing on screen
###

# We can import modules of Python to use them on our code.
# On this case, we import the module "os" which allows the use of functions related with the os
from os import system

# system() allows the execution of a command on the terminal.
# On this case we use it to clear the screen
if system("clear") != 0: system("cls")

# This is a basic example of how to print a text on screen
print("¡Hi!")

# You can use simple quote marks to print any text
print('This is how you can print a text with simple quote marks')

# You can print multiple elements separated by a coma and a space
print("Python", "is", "great")

# The 'sep' parameter define the way in which the elements are gonna separate when printing
print("Python", "es", "brutal", sep = "-")

# The 'end' parameter define the character that will be printed at the end of the output
print("Esto se imprime", end = "\n") # next line
print("en una línea") # This will be printed in the next line

# You can also print numbers and variables
print(42)

# Example of how to print quotes (")
# You cannot use double quotes inside a string, it will generate a syntax error
# print("This is an inch"")  # ❌ syntax error

# ✅ Solution 1: Use simple quotes for all the string, and use double to show the inch
print('This is an "inch" inside a string with simple quotes')

# ✅ Solution 2: Use \ to include double quotes inside the string if it is made with double too
print("This is an \"inch\" inside a string with double quotes using backslash")

# ✅ Solution 3: Use triple quotes to define the string
print("""This is an "inch" inside a string with triple quotes""")