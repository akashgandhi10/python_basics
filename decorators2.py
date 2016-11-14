def hello(name = "Akash"):
    print ("the hello() function has been executed")

    def greet():
        return "\t this is inside gree function"

    def welcome():
        return "\t this is inside welcome function"

    # print greet()
    # print welcome()
    # print "now again back inside hello"

    if name == "Akash":
        return greet
    else:
        return welcome


hello()

x = hello()

print x

print x()

#NameError greet() scope of the function

#welcome() NameError
