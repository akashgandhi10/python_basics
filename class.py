# class Dog(object):
#     'first class'
#     name = "ramesh"
#
#     def __init__(self, breed):
#         self.breed = breed
#
#     def color(self, color = "white"):
#         self.color = color
#         return color
#
# d = Dog(breed = "lab")
#
# d1 = Dog(breed = "Huskie")
#
# print Dog.name
#
# print d.color(color = "brown")
#
# print d1.color()
#
# print d.breed
#
# print d1.breed
#
# print d.name
#
# print Dog.__doc__
#
# print Dog.__name__
#
# print Dog.__module__
#
# print Dog.__bases__
#
# print Dog.__dict__
#
#
# class Circle(object):
#
#     "Docstring for Circle"
#
#     pi = 3.14
#
#     def __init__(self, radius = 1, perimtr = 2*3.14*20):
#         self.radius = radius
#         self.perimtr = perimtr
#
#     def area(self):
#         return (self.radius**2) * Circle.pi
#
#     def set_attr(self, new_radius):
#         self.radius = new_radius
#         return new_radius
#
#     def get_attr(self):
#         return self.radius
#
    # def perimeter(self):
    #     return 2 * Circle.pi * self.radius

# c = Circle()
#
# print c.radius
#
# c1 = Circle(radius = 10)
#
# print c1.area()
#
# print c1.radius
#
# print c1.set_attr(new_radius = 20)
#
# print c1.radius
#
# print c1.area()
#
# print c.get_attr()
#
# print c1.get_attr()
#
# print c.perimeter()
#
# print c1.perimeter()
#
# print c1.perimtr


#inheritance
# class Animal(object):
#     "Parent class"
#
#     type = "general for animal"
#
#     def __init__(self):
#         print "base class"
#
#     def whoIam(self):
#         print "Animal"
#
#     def eat(self):
#         print "eating"
#
# class Dog(Animal):
#
#     "child class"
#
#     subtype = "dog"
#
#     def __init__(self):
#         print "derived class"
#
#     def whoIam(self):
#         print "Marshal"
#
#     def bark(self):
#         print "bough bou"
#
# animal = Animal()
# dog = Dog()
# animal.whoIam()
# dog.whoIam()
# animal.eat()
# dog.eat()
# dog.bark()
# print Animal.type
# print dog.type
# print dog.subtype
# print type(Animal())
# print type(Dog())
# print Animal.__doc__
# print Dog.__doc__
# #issubclass and isinstance
# print issubclass(Dog, Animal)
# print issubclass(Animal, Dog)
# print isinstance(dog, Dog)
# print isinstance(animal, Dog)
# print isinstance(animal,Animal)
# print isinstance(dog, Animal)

#special method string, lenght and delete
# class Book(object):
#     "To check special methods for class in python"
#
#     def __init__(self, title, author, page):
#         print "Book is created"
#         self.title = title
#         self.author = author
#         self.page = page
#
#     def __str__(self):
#         return "Title: %s, Author: %s, Pages: %s" %(self.title, self.author, self.page)
#
#     def __len__(self):
#         return len(self.page)
#
#     def __del__(self):
#         print "Book has been deleted"
#
# print Book.__doc__
# b = Book("My name is Gandhi", "Akash Gandhi", "159")
# print b
# print len(b)
# del b
# print b

# from __future__ import division
# class Line(object):
#     "homework-1 oop"
#
#     def __init__(self, coor1, coor2):
#         self.coordinate1 = coor1
#         self.coordinate2 = coor2
#
#     def distance(self):
            # x1,y1 = self.coordinate1
            # x2,y2 = self.coordinate2
#         print (((self.coordinate1[0] - self.coordinate2[0])**2 + (self.coordinate1[1] - self.coordinate2[1])**2)**(1/2))
#
#
#     def slope(self):
#         print ((self.coordinate2[1] - self.coordinate1[1]) / (self.coordinate2[0] - self.coordinate1[0]))
#
# l = Line((3,2),(8,10))
# print l.coordinate1
# print l.coordinate2
# print l.coordinate1[0]
# print l.coordinate2[0]
# print l.coordinate1[1]
# print l.coordinate2[1]
# l.distance()
# l.slope()


#homework-2
# from __future__ import division
# class Cylinder(object):
#     "homework-2"
#     pi = 3.14
#
#     def __init__(self, height = 1, radius = 1):
#         self.height = height
#         self.radius = radius
#
#     def volume(self):
#         print (Cylinder.pi * (self.radius**2) * self.height)
#
#     def surfaceArea(self):
#         print ((2 * Cylinder.pi * self.radius * self.height) + (2 * Cylinder.pi * (self.radius**2)))
#
# c = Cylinder(2, 3)
# print c.height
# print c.radius
# c.volume()
# c.surfaceArea()
