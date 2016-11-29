import random

#1
def gensquares(n):
    for i in range(n):
        yield i ** 2
for x in gensquares(10+1):
    print x

print ("")
#2
def rand_num(low, high, n):
    for i in range(n):
        yield random.randint(low, high)

for x in rand_num(1, 10, 12):
    print x


print ("")
#3
s = "hello"
iter_s = iter(s)
print next(iter_s)
print next(iter_s)
print next(iter_s)
print next(iter_s)
print next(iter_s)

#4
my_list = [1,2,3,4,5]

gencomp = (item for item in my_list if item > 3)
print gencomp
#unless like list comprehensive, generator comprehensive return generator object
# print next(gencomp)
# print next(gencomp)
for item in gencomp:
    print item
