# syntax
"""
Functions - basic-function
This module demonstrates the basic syntax and usage of functions in Python.

The syntax for defining a function in Python is as follows:
def function_name(parameters):
    '''docstring'''
    function_body
    return value
"""

# basic function
def greet():
    print("Hello new subscriber")

# function with param
def greet_user(name):
    print(f"Hello {name}, welcome to our channel!")

# function with return values
def add(a, b):
    return a + b

# function with default values
def greet_user(name="Guest"):
    print(f"Hello {name}, welcome to our channel!")

# function returning multiple values
def get_mean_median(numbers):
    mean = sum(numbers) / len(numbers)
    sorted_numbers = sorted(numbers)
    mid = len(numbers) // 2
    if len(numbers) % 2 == 0:
        median = (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        median = sorted_numbers[mid]
    return mean, median

# with pass
def dummy_function():
    pass


"""
Execution Examples
"""

greet()

greet_user("Alice")

added_value = add(5, 7)
print(f"The sum is: {added_value}")

greet_user()

numbers = [1, 2, 3, 4, 5]
mean, median = get_mean_median(numbers)
print(f"Mean: {mean}, Median: {median}")

dummy_function()  # Does nothing