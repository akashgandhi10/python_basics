def gencub(n):
    for i in range(n):
        yield i ** 3

for x in gencub(11):
    print x

#noraml
def fibonacci(n):
    a = 1
    b = 1
    output = []

    for i in range(n):
        output.append(a)
        # a = b
        # b = a + b
        t = a
        a = b
        b = t + a
    return output

print fibonacci(10)


def genfib(n):
    a = 1
    b = 1

    for i in range(n):
        yield a
        t = a
        a = b
        b = t + b

for x in genfib(10):
    print x


def simple_gen():
    for i in range(3):
        yield i

g = simple_gen()

print next(g)
print next(g)
print next(g)
# print next(g)

s = "akash"

for iter_s in s:
    print iter_s

# print next(s)

iter_s = iter(s)

print next(iter_s)
print next(iter_s)
print next(iter_s)
print next(iter_s)
print next(iter_s)
# print next(s)
print next(iter_s)
