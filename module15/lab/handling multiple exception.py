# Lab 5b: Handling Multiple Exceptions
try:
    f = open("nonexistent.txt", "r")
    print(10 / 0)
except FileNotFoundError:
    print("Error: File not found!")
except ZeroDivisionError:
    print("Error: Division by zero!")
