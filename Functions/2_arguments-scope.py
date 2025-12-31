"""
Functions - arguments-scope
This module demonstrates functions with multiple arguments and variable scope in Python.

"""

# Function with two arguments
def multiply(a, b):
    return a * b
result = multiply(4, 5)
print(f"The product is: {result}")

# function with keyword arguments
def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")

introduce(age=30, name="John")


# Demonstrating variable scope
x = 10  # global variable
def scope_test():
    y = 5  # local variable
    print(f"Inside function, x: {x}, y: {y}")

scope_test()
print(f"Outside function, x: {x}")