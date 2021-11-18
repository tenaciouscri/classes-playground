#! /usr/bin/env python3

# PYTHON INHERITANCE
# Inheritance allows us to define a class that inherits
# all the methods and properties from another class.
# - PARENT CLASS is the class being inherited from, also
# called base class.
# - CHILD CLASS is the class that inherits from another
# class, also called derived class.

# CREATE A PARENT CLASS
# Create a class named Person, with firstname and lastname
# properties, and a printname method.

class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    
    def printname(self):
        print(f"Hello, {self.firstname} {self.lastname}!")

# Use the Person class to create an object, and then
# execute the printname method.

p1 = Person("John", "Williams")
p1.printname()

# CREATE A CHILD CLASS
# To create a class that inherits the functionality from
# another class, send the parent class as a parameter
# when creating the child class.

# Create a class named Student, which will inherit the
# properties and methods from the Person class.

class Student(Person):
    pass # when you don't want to add any more properties or methods
# Now the Student class has the same properties and methods
# as the Person class.

# Use the Student class to create an object, and then
# execute the printname method.
p2 = Student("Hans", "Zimmer")
p2.printname()

# ADD THE __INIT__() FUNCTION
# Add the __init__() function to the child class, instead
# of the pass keyword.
class Student(Person):
    # WHEN YOU ADD THE INIT FUNCTION, THE CHILD CLASS WILL NO
    # LONGER INHERIT THE PARENT'S INIT FUNCTION!!!
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

# The child init function overrides the inheritance of the
# parent's init function. To keep the inheritance of the
# parent's init function, add a call to the parent's init
# function.
class Student(Person):
    def __init__(self, firstname, lastname):
        Person.__init__(self, firstname, lastname)
# Now we have successfully added the init function and kept
# the inheritance of the parent class.

# USE THE SUPER() FUNCTION
# Python also has a super() function that will make the child
# class inherita all the methods and properties from its
# parent.
class Student(Person):
    def __init__(self, firstname, lastname):
        super().__init__(firstname, lastname)
# By using the super() function, you do not have to use the
# name of the parent element, it will automatically inherit
# the methods and properties from its parent.

# ADD PROPERTIES
# Add a property called graduationyear to the Student class.
class Student(Person):
    def __init__(self, firstname, lastname):
        super().__init__(firstname, lastname)
        self.graduationyear = 2019
# The year 2019 should be a variable and passed into the
# Student class when creating student objects. To do so, we
# add another parameter in the init function.

# Add a year parameter, and pass the correct year when
# creating objects.
class Student(Person):
    def __init__(self, firstname, lastname, year):
        super().__init__(firstname, lastname)
        self.graduationyear = year

p3 = Student("Danny", "Elfman", 2019)
p3.printname()

# ADD METHODS
# Add a method called welcome to the Student class:
class Student(Person):
    def __init__(self, firstname, lastname, year):
        super().__init__(firstname, lastname)
        self.graduationyear = year
    
    def welcome(self):
        print(f"Welcome, {self.firstname} {self.lastname}, to the class of {self.graduationyear}!")
# If you add a method in the child class with the same name
# as a function in the parent class, the inheritance of the
# parent method will be overridden.

# EXERCISES

# Enter the correct syntax to create a class named Student
# that will inherit properties and methods from a class
# named Person.
class Person:
    def __init__(self, fname):
        self.fname = fname

class Student(Person):
    pass

# Enter the correct syntax to execute the printname method
# of the object x.
class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    def printname(self):
        print(f"Hello, {self.fname} {self.lname}!")

class Student(Person):
    pass

p4 = Student("John", "Powell")
p4.printname()