"""
sorted() - returns a sorted list without modifying the original list.
sort() - sorts the list in place, modifying the original list.
reverse() - reverses the order of the list in place.
copy() - creates a shallow copy of the list.
count() - returns the number of occurrences of a specified value.

"""

# list methods for sorting and reversing
my_list = [5, 2, 9, 1, 5, 6]
print("Original list:", my_list)
# Using sorted() to return a new sorted list
sorted_list = sorted(my_list)
print("Sorted list using sorted():", sorted_list)
print("Original list after sorted():", my_list)  # original list remains unchanged


# Using sort() to sort the list in place
my_list.sort()
print("List after sort() in place:", my_list)
# Using reverse() to reverse the order of the list
my_list.reverse()
print("List after reverse() in place:", my_list)

# Using sorted() with reverse=True to get a descending sorted list
my_list = [5, 2, 9, 1, 5, 6]
desc_sorted_list = sorted(my_list, reverse=True)
print("Descending sorted list using sorted() with reverse=True:", desc_sorted_list)

# why use sorted() vs sort()
# Using sorted() to get a new sorted list
# Using sort() to sort the original list in place

# sort(reverse=True) vs reverse() when to use which
# sort(reverse=True) is used to sort the list in descending order
# reverse() is used to simply reverse the current order of the list

# Using copy() to create a shallow copy of the list
my_list = [1, 2, 3, 4, 5]
copied_list = my_list.copy()
print("Original list:", my_list)
print("Copied list using copy():", copied_list)

# Modifying the copied list to show it doesn't affect the original
copied_list.append(6)
print("Modified copied list:", copied_list)
print("Original list after modifying copied list:", my_list)


# Using count() to count occurrences of a value
my_list = [1, 2, 2, 3, 4, 2, 5]
count_of_twos = my_list.count(2)
print("Count of 2 in the list using count():", count_of_twos)