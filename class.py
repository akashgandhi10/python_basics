class Dog(object):
    'first class'
    name = "ramesh"

    def __init__(self, breed):
        self.breed = breed

    def color(self, color = "white"):
        self.color = color
        return color

d = Dog(breed = "lab")

d1 = Dog(breed = "Huskie")

print Dog.name

print d.color(color = "brown")

print d1.color()

print d.breed

print d1.breed

print d.name

print Dog.__doc__

print Dog.__name__

print Dog.__module__

print Dog.__bases__

print Dog.__dict__


class Circle(object):

    "Docstring for Circle"

    pi = 3.14

    def __init__(self, radius = 1, peri = 2*3.14*20):
        self.radius = radius
        self.peri = peri

    def area(self):
        return (self.radius**2) * Circle.pi

    def set_attr(self, new_radius):
        self.radius = new_radius
        return new_radius

    def get_attr(self):
        return self.radius

    def perimeter(self):
        return 2 * Circle.pi * self.radius

c = Circle()

print c.radius

c1 = Circle(radius = 10)

print c1.area()

print c1.radius

print c1.set_attr(new_radius = 20)

print c1.radius

print c1.area()

print c.get_attr()

print c1.get_attr()

print c.perimeter()

print c1.perimeter()

print c1.peri
