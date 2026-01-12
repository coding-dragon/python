"""
tuple is a built-in data type in Python that represents an ordered collection of items.
stores multiple items in a single variable.
Tuples can contain items of different data types, including integers, strings, and even other tuples

A tuple is a collection which is ordered and unchangeable.
ordered: The items have a defined order, and that order will not change unless you explicitly reorder the tuple.
unchangeable: You cannot change, add, or remove items in a tuple after it has been created.
allowed duplicate values: Since tuples are indexed, they can have items with the same value.

round brackets: Tuples are created by placing items inside round brackets ().

"""

# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)
print("Original tuple:", my_tuple)

# Accessing elements
first_element = my_tuple[0]
print("First element:", first_element)

# len() function to get the length of the tuple
length = len(my_tuple)
print("Length of the tuple:", length)

# type() function to check the data type
tuple_type = type(my_tuple)
print("Data type of my_tuple:", tuple_type)

# tuple constructors
new_tuple = tuple((6, 7, 8, 9, 10))
print("New tuple using constructor:", new_tuple)

# Note: Tuples are immutable, so the following line would raise an error if uncommented
# my_tuple[1] = 20  # This will raise a TypeError
# Demonstrating that tuples are immutable

try:
    my_tuple[1] = 20  # This will raise a TypeError
except TypeError as e:
    print("Error:", e)  