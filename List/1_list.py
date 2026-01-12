"""
list is a built-in data type in Python that represents an ordered collection of items.
stores multiple items in a single variable.
Lists can contain items of different data types, including integers, strings, and even other lists.
Lists are mutable, meaning their contents can be changed after they are created.

ordered: The items have a defined order, and that order will not change unless you explicitly reorder the list.
changeable: You can change, add, and remove items in a list after it has been created.
allowed duplicate values: Since lists are indexed, they can have items with the same value.

"""

# Creating a list
my_list = [1, 2, 3, 4, 5]
print("Original list:", my_list)

# Accessing elements
first_element = my_list[0]
print("First element:", first_element)

# Modifying elements
my_list[1] = 20
print("Modified list:", my_list)

# len() function to get the length of the list
length = len(my_list)
print("Length of the list:", length)

# type() function to check the data type
list_type = type(my_list)
print("Data type of my_list:", list_type)


# list constructors
new_list = list((6, 7, 8, 9, 10))
print("New list using constructor:", new_list)