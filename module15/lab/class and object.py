# Lab 6: Class and Object
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s = Student("Alice", 20)
print("Name:", s.name, "Age:", s.age)
