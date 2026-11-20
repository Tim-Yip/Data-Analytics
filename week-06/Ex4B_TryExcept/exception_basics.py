# Value Error
try:
    x = int("Hello, World!")
except ValueError:
    print("ValueError: Cannot convert to an integer.")
else:
    print(x)
finally:
    print("Let's try another one...")

# Name Error
try:
    x = computer
except NameError:
    print("NameError: Variable has not been defined.")
else:
    print(x)
finally:
    print("Let's try another one...")

# Type Error
try:
    x = "computer" + 5
except TypeError:
    print("TypeError: Cannot add an integer to a string.")
else:
    print(x)
finally:
    print("Let's try another one...")

# Syntax Error
try:
    exec("x = 5 x 6")
except SyntaxError:
    print("SyntaxError: Invalid multiplication operator.")
else:
    print(x)
finally:
    print("Let's try another one...")