#  Step 1: Define the tuple
my_tuple = (1, "Python", 3.14, True)

#  Step 2: Access elements using indexing
print(my_tuple[0])    # First element → 1
print(my_tuple[1])    # Second element → "Python"
print(my_tuple[-1])   # Last element → True

#  Step 3: Slicing
print(my_tuple[0:3])  # Elements from index 0 to 2 → (1, "Python", 3.14)

#  Step 4: Access values between index 1 and 5
sample_tuple = (10, 20, 30, 40, 50, 60)
print(sample_tuple[1:5])    # (20, 30, 40, 50)

#  Step 5: Access alternate values between index 1 and 5
print(sample_tuple[1:5:2])  # (20, 40)