"""
List items are indexed and you can access them by referring to the index number.
"""

# accessing elements in a list
my_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']
print("Original list:", my_list)

# Accessing the first element
first_element = my_list[0]
print("First element:", first_element)

# negative indexing to access elements from the end
# Accessing the last element
last_element = my_list[-1]
print("Last element:", last_element)


# Slicing a list to get a subset of elements
subset = my_list[1:4]  # from index 1 to index 3
print("Subset of the list (index 1 to 3):", subset) 

# Accessing every second element
every_second_element = my_list[::2]
print("Every second element:", every_second_element)

# Accessing elements using a loop
print("Accessing elements using a loop:")
for item in my_list:
    print(item)
