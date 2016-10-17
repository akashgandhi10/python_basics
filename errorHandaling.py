print("1")

try:
    print (2 + "h")
except:
    print("hey you have got something wrong")

print("2")

try:
    print (2 + "h")
except TypeError:
    print("hey you have got something wrong")

print("3")

try:
    print ("hey")
except:
    print("hey you have got something wrong")
else:
    print("done")

print("4")

try:
    print (2 + "hey")
except:
    print("hey you have got something wrong")
else:
    print("done")
finally:
    print("this finally part will always going to be printed")

print("5")

try:
    print ("hey")
except:
    print("hey you have got something wrong")
else:
    print("done")
finally:
    print("this finally part will always going to be printed")

print("6")

try:
    print (2 + "hey")
except:
    print ("make it write")
finally:
    print("hey you have got something wrong")

print("7")

def errorHandling():
    try:
        a = int(raw_input("type any number: "))
        print a
    except:
        print("try again with int")
errorHandling()

print("8")

def errorHandling1():
    try:
        a = int(raw_input("type any number: "))
        print a
    except:
        a = int(raw_input("try again here : "))
    else:
        print("done")
errorHandling1()

print ("9")

def errorHandling2():
    while True:
        try:
            a = int(raw_input("type any number: "))
        except:
            print("make it right dude, try again")
            continue
        else:
            print("done")
            break
        finally:
            print("finally")

    print a
errorHandling2()

print("10")

try:
    f = open("errorHandling.txt", "r")
    f.read()
except TypeError:
    print("i won't take place")
except IOError:
    print("perfect exception")
else:
    print("i am tp, bcz wront code in try exception ll take place")
finally:
    print("finally done")
