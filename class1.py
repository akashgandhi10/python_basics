class Load(object):
    "naiti load"
    __counter = 0
    c=0

    def __init__(self, x=1.0):
        # abs_method()
        self.x = x

    def square(self):
        return self.x**2

    @staticmethod
    def static_method():
        c += 1

# del a

Load.static_method()
Load.c
a = Load()
b = Load(2.0)

a.x = 1
b.x = 2

b.x = 6

b.__counter = 100
a.c
print a.square()

# overloading:
# overriding:

# class Animals(object):
#
#     def __init__(self, name):
#         self.name = name
#
#     @abstractmethod
#     def sound(self):
#         pass
#
# class Cow(Animals):
#     def __init__(self):
#         pass
#
#     def sound(self):
#         print 'moooo'
#
# class Dog(Animals):
#     def sound(self):
#         print 'bhowwww'
#
# def inp():
#     i = random.randint(0, 100)
#     if i%5 == 0:
#         a = Cow()
#     else:
#         a = Dog()
#
#     a = input('d;b;sdbg')
#     if a == 1:
#
# # Cow().sound1()
# # Dog().sound2()
#
# #
# # class Calculator(object):
# #     def __init__(self):
# #         pass
# #
# #     def add(self, x, y):
# #         return x + y
# #
# #     def add(self, x, y, z):
# #         return x + y + z
# # def func1(*args, **kwargs):
