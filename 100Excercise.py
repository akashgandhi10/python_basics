# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.
#
# l = []
# for i in range(2000,3201):
#     if i % 7 == 0 and i % 5 != 0:
#         l.append(str(i))
#
# print ','.join(l)
#
# Question:
# With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
#
# def dictsqure(n):
#     d = {}
#     for i in range(1,n+1):
#         d[i] = i**2
#     print d
# dictsqure(8)
#
# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')
#
#
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
#
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
#
# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
#
# Example
# Suppose the following inputs are given to the program:
# 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
#
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
#
# Question:
# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be:
# bag,hello,without,world
#
# def sorting():
#     w = raw_input("word sequence: ")
#     lw = w.split(",")
#     lw.sort()
#     print ",".join(lw)
# sorting()
#
# Question 9
# Level 2
#
# Question
# Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
# Suppose the following input is supplied to the program:
# Hello world
# Practice makes perfect
# Then, the output should be:
# HELLO WORLD
# PRACTICE MAKES PERFECT
#
# def multiline():
#     # lines = []
#     #
#     # while True:
#     #     line = raw_input()
#     #     if line:
#     #
#     #         lines.append(line)
#     #     else:
#     #         break
#     # print '\n'.join(lines).upper()
#     n = 5
#     lines = ""
#     for i in range(n):
#         lines += raw_input() + "\n"
#     print "\n"
#     print lines.upper()
# multiline()
#
# def upperline():
#     no_of_lines = 5
#     lines1 = ""
#     for i in xrange(5):
#         lines1+=raw_input()+"\n"
#     print lines1.upper()
#
#     lines = []
#     while True:
#         line = raw_input()
#         if line:
#             lines.append(line)
#         else:
#             break
#
#     text = '\n'.join(lines)
#     print text.upper()
# upperline()
#
# Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world
#
# def rmduplicate():
#     s = raw_input()
#     l = s.split()
#     # # print l
#     # l1 = []
#     # for i in l:
#     #     if i not in l1:
#     #         l1.append(i)
#     # l1.sort()
#     # # print l1
#     # print " ".join(l1)
#     print ' '.join(sorted(list(set(l))))
# rmduplicate()
#
# Question:
# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
# Example:
# 0100,0011,1010,1001
# Then the output should be:
# 1010
# Notes: Assume the data is input by console.
#
# def binary():
#     l = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011', '1100',
#         '1101', '1110', '1111']
#     l1 = []
#     while True:
#         b = raw_input()
#         if b:
#             if b in l:
#                 l1.append(b)
#         else:
#             break
#     total = ""
#     for i,j in enumerate(l1):
#         # if i == 0:
#         t = int(j[0])*8 + int(j[1])*4 + int(j[2])*2 + int(j[3])
#         # elif i == 1:
#         #     t = int(j[1])*4
#         # elif i == 2:
#         #     t = int(j[2])*2
#         # else:
#         #     t = int(j[3])
#         # total += t
#         total += str(t) + ', '
#     total = total[:-2]
#     print ','.join(l1)
#     print total
#
# binary()
#
# def binary():
#     l = [x for x in raw_input().split(",")]
#     l1 = []
#
#     for p in l:
#
#         intp = int(p, 2)
#         if not intp%5:
#             l1.append(p)
#
#     print ",".join(l1)
# binary()
#
#
# Question:
# Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.
#
# def alleven():
#     l = range(1000,3001)
#     l1 = []
#     for i in l:
#         i = str(i)
#         if int(i[0]) % 2 == 0 and int(i[1]) % 2 == 0 and int(i[2]) % 2 == 0 and int(i[3]) % 2 == 0:
#             l1.append(i)
#     print ",".join(l1)
# alleven()
#
# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3
# import string
# def cal():
#     l = [x for x in raw_input().split()]
#     n = ""
#     w = ""
#     atoz = string.ascii_lowercase
#     print atoz
#     for i in l:
#         try:
#             if int(i):
#                 n += i
#         except:
#             for j in i:
#                 if j in atoz:
#                     w += j
#     print ("LETTERS %s \nDIGITS %s" %(len(w),len(n)))
# cal()
# def cal():
#     s = raw_input()
#     d = {"DIGITS": 0, "LETTERS": 0}
#     for i in s:
#         if i.isdigit():
#             d["DIGITS"] += 1
#         elif i.isalpha():
#             d["LETTERS"] += 1
#         else:
#             pass
#     l = d.values()
#     print ("LETTERS %s \nDIGITS %s" %(l[1],l[0]))
# cal()
#
# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9
#
# def upper_lower():
#     s = raw_input()
#     d = {"UPPER": 0, "LOWER": 0}
#     for i in s:
#         if i.isupper():
#             d["UPPER"] += 1
#         elif i.islower():
#             d["LOWER"] += 1
#         else:
#             pass
#     l = d.values()
#     print ("LOWER %s \nUPPER %s" %(l[1],l[0]))
# upper_lower()

# Question
# Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
# Suppose the following input is supplied to the program:
# Hello world
# Practice makes perfect
# Then, the output should be:
# HELLO WORLD
# PRACTICE MAKES PERFECT
#
# def upper_():
#     # l = [x for x in raw_input().upper()]
#     # print l
#     l = []
#     while True:
#         s = raw_input()
#         if s:
#             s = s.upper()
#             l.append(s)
#         else:
#             break
#     # for i in l:
#     #     print i
#     print "\n".join(l)
# upper_()


# Question 15
# Level 2
#
# Question:
# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106


#
# def equ():
#     n = raw_input()
#     return int(n) + int(n+n) + int(n+n+n) + int(n+n+n+n)
# print equ()

# Question:
# Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
# Suppose the following input is supplied to the program:
# 1,2,3,4,5,6,7,8,9
# Then, the output should be:
# 1,3,5,7,9

#
# print ",".join([x for x in raw_input().split(",") if int(x) % 2 != 0])

# Question:
# Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
# D 100
# W 200

# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
# D 300
# D 300
# W 200
# D 100
# Then, the output should be:
# 500

# def bank():
#     total = 0
#     while True:
#         trans = raw_input()
#
#         if not trans:
#             break
#         try:
#             n = int(trans[2:])
#             if n:
#                 if trans[1] == " ":
#                     if trans[0].upper() == "D":
#                         total += n
#                     elif trans[0].upper() == "W":
#                         total -= n
#                     else:
#                         pass
#         except ValueError:
#             print "please try valid amount for transaction"
#
#     print total
# bank
# Question:
# A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
# Following are the criteria for checking the password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 1. At least 1 letter between [A-Z]
# 3. At least 1 character from [$#@]
# 4. Minimum length of transaction password: 6
# 5. Maximum length of transaction password: 12
# Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
# Example
# If the following passwords are given as input to the program:
# ABd1234@1,a F1#,2w3E*,2We3345
# Then, the output of the program should be:
# ABd1234@1
# import string
# def one(i):
#     atoz = string.ascii_lowercase
#     for x in atoz:
#         if x in i:
#             return True
#
# def two(i):
#     for x in range(0,10):
#         if str(x) in i:
#             return True
#
# def three(i):
#     ATOZ = string.uppercase
#     for x in ATOZ:
#         if x in i:
#             return True
#
# def four(i):
#     s = "$#@"
#     for x in s:
#         if x in i:
#             return True
#
# def valid_pass():
#     l = [x for x in raw_input().split(",")]
#     for i in l:
#         if 6 <= len(i) and len(i) <= 12:
#             if one(i) and two(i) and two(i) and three(i) and four(i):
#                 return i
#
# print valid_pass()

# Question:
# You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, age and height are numbers. The tuples are input by console. The sort criteria is:
# 1: Sort based on name;
# 2: Then sort based on age;
# 3: Then sort by score.
# The priority is that name > age > score.
# If the following tuples are given as input to the program:
# Tom,19,80
# John,21,90
# John,20,95
# John,20,90
# Jony,17,93
# Jony,17,91
# Jony,16,90
# Json,21,85

# Then, the output of the program should be:
# [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
# from operator import itemgetter
# def sort_tuple():
#     l = []
#     while True:
#         s = raw_input()
#         if not s:
#             break
#         t = tuple(s.split(","))
#         l.append(t)
#
#     print sorted(l, key = lambda x: (x[0],x[1],x[2]))
#     print sorted(l, key = itemgetter(0,1,2))
# sort_tuple()



# Question
# A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
#
# The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.
# Example:
# If the following tuples are given as input to the program:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# Then, the output of the program should be:
# 2
import math
# def distance():
#     up = input("UP ")
#     down = input("DOWN ")
#     left = input("LEFT ")
#     right = input("RIGHT ")
#     x = up - down
#     y = right - left
#     dist = int(math.sqrt((x**2) + (y**2)))
#
#     print dist
# distance()

# def distance():
#     poss = [0,0]
#     while True:
#         s = raw_input()
#         if not s:
#             break
#         l = s.split(" ")
#         movement = l[0]
#         direction = int(l[1])
#
#         if movement == "UP":
#             poss[0] += direction
#         elif movement == "DOWN":
#             poss[0] -= direction
#         elif movement == "LEFT":
#             poss[1] -= direction
#         elif movement == "RIGHT":
#             poss[1] += direction
#         else:
#             pass
#     dist = int(round(math.sqrt((poss[0]**2) + (poss[1]**2))))
#     print dist
#
# distance()

# Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically.
# Suppose the following input is supplied to the program:
# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
# Then, the output should be:
# 2:2
# 3.:1
# 3?:1
# New:1
# Python:5
# Read:1
# and:1
# between:1
# choosing:1
# or:2
# to:1

# def frequency():
#     l = [x for x in raw_input().split(" ")]
#     d = {}
#     for i in l:
#         if i not in d:
#             d[i] = 1
#         else:
#             d[i] += 1
#     # for key, value in d.items() :
#     #     print key + ":",value
#     dsortkey = sorted(d.keys())
#     for i in dsortkey:
#         print "%s: %d" %(i,d[i])
#
#
# frequency()
