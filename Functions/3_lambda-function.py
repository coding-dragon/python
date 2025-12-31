"""
Functions - lambda-function
This module demonstrates the use of lambda functions in Python.
it is a small anonymous function that can take any number of arguments, but can only have one expression.

"""

# Lambda function to multiply a number by 2
lambda_multipleOf2 = lambda a: a * 2
result = lambda_multipleOf2(5)
print(result)

# Lambda function to add two numbers
lambda_add = lambda a, b: a + b
result = lambda_add(3, 7)
print(result)

# Lambda function to find the maximum of two numbers
lambda_max = lambda a, b: a if a > b else b
result = lambda_max(10, 20)
print(result)

# Lambda function to create a multiplier (closure example)
def myFunc(n):
    return lambda a: a * n

multiplier_11 = myFunc(11)
result_22 = multiplier_11(2) 
print(result_22)
result_33 = multiplier_11(3) 
print(result_33)


# lambda function inside another function
def apply_operation(x, y, operation):
    return operation(x, y)

result = apply_operation(6, 4, lambda a, b: a - b)
print(result)


# lambda function with built in methods
# lambda function with filter to get even numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

# lambda function with map to square each number in a list
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)

# lambda function with reduce to calculate the addition of all numbers in a list
from functools import reduce
sum_all = reduce(lambda x, y: x + y, numbers)
print(sum_all)