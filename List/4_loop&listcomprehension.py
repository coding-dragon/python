"""
Loop and List Comprehension Examples

Looping through a list allows you to perform operations on each element.

List comprehension offers a shorter syntax when you want to create a new list 
based on the values of an existing list.

"""

# Looping through a list
my_list = ['a', 'b', 'c', 'd', 'e']
print("Looping through the list:")
for item in my_list:
    print(item)


# Accessing elements using enumerate to get index and value
print("Accessing elements with index using enumerate:")
for index, item in enumerate(my_list):
    print(f"Index {index}: {item}")

# Accessing elements using range and len
print("Accessing elements with index using range and len:")
for i in range(len(my_list)):
    print(f"Index {i}: {my_list[i]}")


# Using list comprehension to create a modified list
squared_list = [x**2 for x in range(6)]
print("Squared list using list comprehension:", squared_list)

# Using the map function to create a modified list
doubled_list = list(map(lambda x: x * 2, range(6)))
print("Doubled list using map function:", doubled_list)

# Using the filter function to create a filtered list
even_numbers = list(filter(lambda x: x % 2 == 0, range(10)))
print("Even numbers using filter function:", even_numbers)

# Using list comprehension to filter and modify a list
modified_list = [x * 3 for x in range(10) if x % 2 == 0]
print("Modified list (tripled even numbers) using list comprehension:", modified_list)
