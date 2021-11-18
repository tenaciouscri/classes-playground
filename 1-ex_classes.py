#! /usr/bin/env python3

# CREATE CLASS
# Create a class named MyClass, with a property named x:
class MyClass:
    x = 5

# CREATE OBJECT
# Create an object named p1, and print the value of x
p1 = MyClass()
print(p1.x)

# THE __INIT__() FUNCTION
# __init__ is always executed when the class is being initiated.
# It's used to assign values to object properties, or other
# operations that are necessary to do when the object is being
# created.

# Create a class named Person, use the __init__() function to
# assign values for name and age.
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

p1 = Person("Cristina", 30)
print(p1.name)
print(p1.age)

# OBJECT METHODS
# Objects can contain methods. Methods in objects are functions
# that belong to the object.

# Insert a function that prints a greeting, and execute it on the
# p1 object.
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    def greeting(self):
        print(f"Hello, {self.name}!")

p1 = Person("Cristina", 30)
p1.greeting()

# THE SELF PARAMETER
# The self parameter is a reference to the current instance of the
# class, and is used to access variables that belongs to the class.
# It does not have to be named self, you can call it whatever you
# like, but it has to be the first parameter of any function in the class:

# Use the words mysillyobject and abc instead of self:
class Person:
    def __init__(mysillyobject, name: str, age: int):
        mysillyobject.name = name
        mysillyobject.age = age
    
    def greeting(abc):
        print(f"Hello, {abc.name}!")

p1 = Person("Cristina", 30)
p1.greeting()

# MODIFY OBJECT PROPERTIES
# Set the age of p1 to 40

p1.age = 40

# DELETE OBJECT PROPERTIES
# You can delete properties on objects by using the del keyword.

# Delete the age property from the p1 object.

del p1.age

# DELETE OBJECTS
# You can delete objects by using the del keyword.

# Delete the p1 object.

del p1

# THE PASS STATEMENT
# class definitions cannot be empty, but if you for some reason have
# a class definition with no content, put it in the pass statement to
# avoid getting an error.
class Person:
    pass

# EXERCISES

# Create a class named MyClass
class MyClass:
    x = 5

# Create an object MyClass called p1
class MyClass:
    x = 5

p1 = MyClass()

# Use the p1 object to print the value of x
class MyClass:
    x = 5

p1 = MyClass()
print(p1.x)

# Enter the correct syntax to assign an init function to a class
class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age
