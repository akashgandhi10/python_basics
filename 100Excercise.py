# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

# l = []
# for i in range(2000,3201):
#     if i % 7 == 0 and i % 5 != 0:
#         l.append(str(i))
#
# print ','.join(l)

# Question:
# With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

# def dictsqure(n):
#     d = {}
#     for i in range(1,n+1):
#         d[i] = i**2
#     print d
# dictsqure(8)

# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')


# def comma_separated():
#     n = raw_input("type in comma_separated numbers: ")
#     l = n.split(',')
#     print l
#     t = tuple(l)
#     return t
# print comma_separated()
#
# Question:
# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

# class atleast(object):
#     "getString and printString"
#
#     def __init__(self):
#         print "i am init fucker"
#         self.s = ""
#     def getString(self):
#         self.s = raw_input("write string: ")
#     def printString(self):
#         print self.s.upper()
#
# a = atleast()
# print atleast.__name__
# print atleast.__doc__
# print atleast.__module__
# print atleast.__bases__
# print atleast.__dict__
# a.getString()
# a.printString()
#
# Question:
# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.
# Example
# Let us assume the following comma separated input sequence is given to the program:
# 100,150,180
# The output of the program should be:
# 18,22,24
# from __future__ import division
# def squareroot(C = 50, H = 30):
#     D = raw_input("comma_separated sequence: ")
#     l = D.split(",")
#     l1 = []
#     ql = ""
#     for i in l:
#         i = int(i)
#         Q = ((2 * C * i)/H)**(1/2.0)
#         Q = str(int(Q))
#         l1.append(Q)
#         ql = ql + Q + ","
#     ql = ql [:-1]
#     print l1
#     print ",".join(l1)
#     print ql
#
# squareroot()

# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
#
# Example
# Suppose the following inputs are given to the program:
# 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

# print [[i*j for i in range (5)] for j in range (3)]
#
# def two_dimensional_array(y, x):
#     l = [[] for _ in xrange(y)]
#     count = 0
#
#     for i in range(y):
#         for j in range(x):
#             l[i].append(i*j)
#
#     print l
#
# two_dimensional_array(3, 5)

# Question:
# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be:
# bag,hello,without,world

def sorting():
    w = raw_input("word sequence: ")
    lw = w.split(",")
    lw.sort()
    print ",".join(lw)
sorting()
