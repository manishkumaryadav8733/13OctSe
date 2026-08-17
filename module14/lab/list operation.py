# Concatenation
list1 = [1, 2, 3]
list2 = [4, 5]
print(list1 + list2)  # [1, 2, 3, 4, 5]

# Repetition
print(list1 * 2)  # [1, 2, 3, 1, 2, 3]

# Membership
print(2 in list1)  # True

# Append and Insert
list1.append(6)        # Adds 6 at the end
list1.insert(1, 10)    # Inserts 10 at index 1
print(list1)

# Remove and Pop
list1.remove(10)       # Removes the first occurrence of 10
list1.pop()            # Removes the last element
print(list1)