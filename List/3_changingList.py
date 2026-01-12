"""
This script demonstrates various methods to change, add, and remove elements in a Python list.

| index | method | description |
|-------|--------|-------------|
| 1     | via index | Modify an existing element by accessing it via its index. |
| 2     | append() | Add an element at the end of the list. |
| 3     | insert() | Insert an element at a specific index. |
| 4     | extend() | Add multiple elements at the end of the list. |
| 5     | remove() | Remove a specific element by value. |
| 6     | pop() | Remove an element at a specific index and return it. |
| 7     | del | Delete an element at a specific index. |
| 8     | clear() | Remove all elements from the list. |

"""

# changing list elements
my_list = [10, 20, 30, 40, 50]
print("Original list:", my_list)

# Changing the second element
my_list[1] = 200
print("List after changing the second element:", my_list)


# Adding elements to a list
# Using append() to add an element at the end
my_list.append(60)
print("List after appending 60:", my_list)

# Using insert() to add an element at a specific position
my_list.insert(2, 25)  # inserting 25 at index 2
print("List after inserting 25 at index 2:", my_list)

# Using extend() to add multiple elements at the end
my_list.extend([70, 80, 90])
print("List after extending with [70, 80, 90]:", my_list)


# Removing elements from a list
# Using remove() to remove a specific element
my_list.remove(30)
print("List after removing 30:", my_list)


# Using pop() to remove an element at a specific index
popped_element = my_list.pop(3)  # removing element at index 3
print("Popped element at index 3:", popped_element)
print("List after popping element at index 3:", my_list)


# Using del to remove an element at a specific index
del my_list[0]  # deleting element at index 0
print("List after deleting element at index 0:", my_list)

# Using clear() to remove all elements from the list
my_list.clear()
print("List after clearing all elements:", my_list)


# slice assignment to change multiple elements
my_list = [1, 2, 3, 4, 5]
print("Original list for slice assignment:", my_list)
my_list[1:4] = [20, 30, 40]  #
print("List after slice assignment (index 1 to 3):", my_list)