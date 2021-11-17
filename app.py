#! /usr/bin/env python3

class NameOfClass():
    
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2
    
    def some_method(self):
        # perform some action
        print(self.param1)

# BASICS

class Dog(): # keyword class, created our own sample class
    # just like a function, except when it's inside a class,
    # it's referred as a method. This is a special method
    # called the __init__ method, which is going to be called
    # upon when you create an instance of the class.
    # We always start off with the self keyword, which connects
    # the method to the instance. Then we pass in any
    # attributes we want the user to define.
    def __init__(self, breed, name, spots: bool):# init = constructor, (attributes)
        
        # Attributes
        # We take in the argument
        # Assign it using self.attribute_name
        self.breed = breed
        self.name = name
        # Expect boolean True/False
        self.spots = spots
        
my_dog = Dog(breed = "Mix", name = "Jake", spots = False) # instance of class
print(my_dog.breed)
print(my_dog.name)
print(my_dog.spots)

# USING METHODS

class Dog():
    
    # CLASS OBJECT ATTRIBUTE: SAME FOR ANY INSTANCE.
    # Attribute defined at a class-object level.
    species = "mammal"
    
    def __init__(self, breed, name):
        
        self.breed = breed
        self.name = name
    
    # METHODS (operations, actions):
    # Functions defined inside the body of the class and used to
    # perform operations that sometimes utilize the actual attributes
    # of the object we've created. In other words, they're functions
    # acting on an object that take the object itself into account
    # through the use of the self argument/keyword.
    def bark(self, number): # Methods can take outside arguments
        print("WOOF! My name is {} and the number is {}!".format(self.name, number))

my_dog = Dog("Mix", "Jake")
print(my_dog.breed) 
# Attributes never has () because they don't have anything to execute.
# They're rather a characteristic of the object that you call back.
print(my_dog.name)
# Even though we haven't defined it, it's always available
# and the same for any instance.
print(my_dog.species) 

# Methods will need to be executed, therefore we'll need to use ()
my_dog.bark(7)

# ANOTHER EXAMPLE

class Circle():
    
    # CLASS OBJECT ATTRIBUTE
    pi = 3.14
    
    def __init__(self, radius = 1): # default values possible
        
        self.radius = radius
        self.area = radius * radius * Circle.pi # can also be self.pi
    
    # METHOD
    def get_circumference(self):
        return self.radius * Circle.pi * 2

my_circle = Circle(30)

print(my_circle.pi)
print(my_circle.radius)
print(my_circle.area)
print(my_circle.get_circumference())

# INHERITANCE

class Animal(): # BASE CLASS
    
    def __init__(self):
        print("ANIMAL CREATED")
    
    def who_am_i(self):
        print("I am an animal")
    
    def eat(self):
        print("I am eating")

class Dog(Animal): # DERIVED CLASS
    
    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")
    
    # Overriding older method
    def who_am_i(self):
        print("I am a dog")
    
    # Add on methods
    def bark(self):
        print("WOOF!")

my_dog = Dog()

my_dog.eat()
my_dog.who_am_i()
my_dog.bark()

# POLYMORPHISM

# Two classes, each of them with the speak method.
# When called, each object's speak method returns a
# result that is unique to the object.
class Dog():
    
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return self.name + " says woof!"

class Cat():
    
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return self.name + " says meow!"

jake = Dog("Jake")
eva = Cat("Eva")

print(jake.speak()) # Don't forget ()!
print(eva.speak())

# Demonstrating polymorphism through a for loop
for pet in [jake, eva]:
    
    print(type(pet))
    print(pet.speak())

# Demonstrating polymorphism through a function
def pet_speak(pet):
    print(pet.speak())

pet_speak(jake)
pet_speak(eva)

class Animal():
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")

class Dog(Animal):
    
    def speak(self):
        return self.name + " says woof!"

class Cat(Animal):
    
    def speak(self):
        return self.name + " says meow!"

fido = Dog("Fido")
musya = Cat("Musya")

print(fido.speak())
print(musya.speak())

# SPECIAL METHODS

# Special methods allow us to use some built-in operations
# in Python, such as the length function or the print
# function with our own user created objects.

mylist = [1, 2, 3]

len(mylist)

# What if we wanted to check the length of our own object?

class Book():
    
    def __init__(self, title, author, pages): # init is a special method
        
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self): # string representation of the object itself
        return f"{self.title} by {self.author}"
    
    def __len__(self):
        return self.pages
    
    def __del__(self):
        print("A book object has been deleted")

b = Book("Python rocks", "Me", 200)
print(b) # This will only print the position of b in our memory
print(len(b))

# What if we want to delete a book from our memory?
del b # if you ask for b again, it's going to say that b is not defined
# If you want anything specific to happen upon deleting b,
# you'll have to define __del__ (line 217)

