
# accessing elements in a tuple
my_tuple = (10, 20, 30, 40, 50)
print("Original tuple:", my_tuple)

# Accessing the first element
first_element = my_tuple[0]
print("First element:", first_element)

# negative indexing to access elements from the end
# Accessing the last element
last_element = my_tuple[-1]
print("Last element:", last_element)


# Slicing a tuple to get a subset of elements
subset = my_tuple[1:4]  # from index 1 to index 3
print("Subset of the tuple (index 1 to 3):", subset)

# Accessing every second element
every_second_element = my_tuple[::2]
print("Every second element:", every_second_element)


# Accessing elements using a loop
print("Accessing elements using a loop:")
for item in my_tuple:
    print(item)