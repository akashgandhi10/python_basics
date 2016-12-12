from collections import namedtuple

t = (1,2,3)
print t[0]

Dog1 = namedtuple("Dog", "age color name")
ashish = Dog1(age=3, color="brown", name="ashish")
pandya = Dog1(age=1, color="black", name="pandya")
print ashish
print pandya
print ashish.age
print ashish.color
print ashish.name
print ashish[0]
print ashish[1]
print ashish[2]
print pandya.color
