# Updating a value
my_dict["age"] = 26
print(my_dict)

# Merging two lists into a dictionary
keys = ["a", "b", "c"]
values = [1, 2, 3]
merged_dict = dict(zip(keys, values))
print(merged_dict)

# Counting occurrences of characters in a string
text = "hello"
char_count = {}
for char in text:
    char_count[char] = char_count.get(char, 0) + 1
print(char_count)  # {'h':1, 'e':1, 'l':2, 'o':1}