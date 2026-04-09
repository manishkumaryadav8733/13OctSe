# Iterating over a list
for item in list1:
    print(item)

# Sorting
numbers = [5, 2, 9, 1]
numbers.sort()         # Sorts in place
print(numbers)

# Using sorted() (returns a new list)
print(sorted(numbers, reverse=True))  # Descending order

# Reversing
numbers.reverse()
print(numbers)