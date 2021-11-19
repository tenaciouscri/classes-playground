#! /usr/bin/env python3

from math import pi

# PROBLEM 1

# Fill in the Line class methods to coordinate as a pair of
# tuples and return the slope and distance of the line.
class Line:
    
    def __init__(self, coor1: tuple, coor2: tuple):
        self.coor1 = coor1 # could also be unpacked with self.coor1 - coor1[0]
        self.coor2 = coor2
    
    # Reminder: coor1 and coor2 are tuples!
    
    def distance(self):
        # tuple unpacking needed
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        # square root of pow(x2-x1) + pow(y2-y1)
        return ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    
    def slope(self):
        # tuple unpacking still needed
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        # y2 - y1 / x2 - x1
        return (y2 - y1) / (x2 - x1)


coordinate1 = (3, 2)
coordinate2 = (8, 10)

li = Line(coordinate1, coordinate2)

print(li.distance())

print(li.slope())

# PROBLEM 2

# Fill in the class.

class Cylinder:
    
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        # pi * r**2 * h
        return pi * self.radius**2 * self.height
    
    def surface_area(self):
        # 2 * pi * r * (r + h)
        return 2 * pi * self.radius * (self.radius + self.height)

c = Cylinder(2, 3)

print(c.volume())

print(c.surface_area())