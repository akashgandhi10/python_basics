def func():
    return 1

print func()

x = func

print x()

s = "this is global variable"

def func1():
    print locals()

func1()
print globals()
print globals().keys()
print globals()["s"]

def hello(name = "Akash"):
    return "Hello " + name

print hello()

greet = hello

print greet()

del hello

#NameError print hello() it's not longer exists but greet() does

print greet()
