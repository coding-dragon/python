"""
This script demonstrates various methods to change, add, and remove elements in a Python tuple.

| index | method | description |
|-------|--------|-------------|


"""

# changing tuple elements
my_tuple = (10, 20, 30, 40, 50)
print("Original tuple:", my_tuple)

# Since tuples are immutable, we cannot change elements directly.
# However, we can convert the tuple to a list, make changes, and convert it back
temp_list = list(my_tuple)
# Changing the second element
temp_list[1] = 200
# Converting back to tuple
my_tuple = tuple(temp_list)
print("Tuple after changing the second element:", my_tuple)

# Adding elements to a tuple
# Converting to list to add elements
temp_list = list(my_tuple)
# Adding an element at the end
temp_list.append(60)
# Converting back to tuple
my_tuple = tuple(temp_list)
print("Tuple after adding 60:", my_tuple)


# Inserting an element at a specific position
temp_list = list(my_tuple)
temp_list.insert(2, 25)  # inserting 25 at index 2
my_tuple = tuple(temp_list)
print("Tuple after inserting 25 at index 2:", my_tuple)


# Removing elements from a tuple
# Converting to list to remove elements
temp_list = list(my_tuple)
# Removing a specific element
temp_list.remove(30)
my_tuple = tuple(temp_list)
print("Tuple after removing 30:", my_tuple)


# Removing an element at a specific index
temp_list = list(my_tuple)
popped_element = temp_list.pop(3)  # removing element at index 3
my_tuple = tuple(temp_list)
print("Popped element at index 3:", popped_element)
print("Tuple after popping element at index 3:", my_tuple)

# Deleting an element at a specific index
temp_list = list(my_tuple)
del temp_list[0]  # deleting element at index 0
my_tuple = tuple(temp_list)
print("Tuple after deleting element at index 0:", my_tuple)
# Note: Tuples do not have a clear() method since they are immutable.

