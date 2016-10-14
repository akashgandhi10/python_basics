"""
# Functions

def myFunc():
	return True


def myFunc1(a, b):
	return a + b


def noReturnValue():
	return


def defaultParamValues(a=5):
	return a


def mix(a, b=10):
	return a + b


print noReturnValue()
print defaultParamValues()
print defaultParamValues('akash')
print mix(5)
print mix(5, 2500)

# Given an integer n, print sum of 1 to n, using functions:

def sigma(n):
	if n == 1:
		return 1
	return n + sigma(n-1)


print sigma(10)



# Fibonacci 0,1,1,2,3,5

myList = [0, 1]
def fib(n):
	global myList
	if n < len(myList):
		return myList[n]
	retVal = fib(n-1) + fib(n-2)
	myList.append(retVal)
	return retVal

print fib(100)

#ex-1
print(" ")

def maxoftwo(a,b):
	if a > b:
		return a
	return b

def maxofthree(a,b,c):
	return maxoftwo(c,maxoftwo(a,b))

print maxofthree(10,20,30)

print max(10,20,30)

#ex-2

print(" ")
def sum(numbers):
	total=0
	for x in numbers:
		total += x
	return total

print(sum((8,10,18)))

#ex-3

print(" ")
def multiply(numbers):
	total=1
	for i in numbers:
		total *= i
	return total

print multiply((5,10,10))

print(" ")
def revString(myString):
	'''revStr1 = ""
	index = len(myString)
	while index > 0:
		revStr1 += myString[index-1]
		index -= 1
	#return revStr1'''

	l = len(myString)
	retVal = ""
	for i in range(1, l+1):
		retVal = retVal + myString[-i]
	print retVal

print revString("akash")




http://www.w3resource.com/python-exercises/python-functions-exercises.php
#ex-4

def revString(myString):

	revString1 = ""
	lenght = len(myString)
	for i in range(1,lenght+1):
		revString1 = revString1 + myString[-i]
	return revString1

print revString("akash")

#palindrome

def palindrome(s):
	index = len(s)	
	#half = myPali[Index/2]
	for i in range(1,index+1):
		if	s[i-1] != s[-i]:
			return ("%s not palindrome" %s)
	return ("%s is palindrome" %s)
	#print("is palindrome")

print palindrome("akashhsakaa")

#ex-5
def factorial(n):
	'''fact = 1
	for i in range(1,n):
		fact = 5 * i
	return fact'''
	if n == 0:
		return 1
	else:
		return n * factorial(n-1)
n = int(input("number : "))
print factorial(n)

#ex-6

def range1(n):

	#range1 = range(s,e)
	
	for i in range(s,e):
		if n == i:
			return "numer exits"
	return "out of range"

s = int(input("eneter first number in range : "))
e = int(input("eneter last number in range : "))
n = int(input("eneter number for check in range : "))

print range1(n)

def range2():

	s = int(input("eneter first number in range : "))
	e = int(input("eneter last number in range : "))
	n1 = int(input("eneter number for check in range : "))
	
	if n1>=s and n1<=e:
		return "numer exits"
	else:
		return "out of range"
'''s = int(input("eneter first number in range : "))
e = int(input("eneter last number in range : "))
n1 = int(input("eneter number for check in range : "))'''


print range2()

print list(set([1,1,1,1,1,1,1,2,2,3,3,4,4,5,5,6,7,8,0,8,7,6,5,4]))

#ex=8
myList = [1,2,2,3,3,4,4,4,4,5,5,5,6,7,7]
def unique(myList):


	newList = []
	#l = len(myList)
	for i in myList:
		if i not in newList:
			newList.append(i)
		
			'''if myList[i-1] == myList[range(i+1,-i)]:
				remove.myList[i-1]
			else:
				newList = myList[i-1]'''
	return newList

print unique(myList)

#Ex-7

def String_test(s):

	d = {"upper case":0, "lower case":0}
	for i in s:
		if i.isupper():
			d["upper case"] += 1
		elif i.islower():
			d["lower case"] += 1
		else:
			pass
	
	print("number of upper case in strng : ", d["upper case"]) 
	print("number of lower case in strng : ", d["lower case"])

String_test("Akash Pravinbhai Gandhi")

#Ex-9

def prime(n):
	
	if n==0 or n==1:
		return False
	elif n==2:
		return "prime"
	else:
		for i in range(2,n-1):
			if n % 2 !=0:
				return "number is prime"
		return "not prime"
		
print prime(int(input("eneter number : ")))

#Fibonaci series : 0,1,1,2,3,5,8,13,21... n= (n-1) + (n=2)

myList = [0,1]
def fib(n):

	#l = len(myList)
	#for i in range(0,n)
	if n < len(myList):
		return myList[n]
	retval = fib(n-1) + fib(n-2)
	myList.append(retval)
	return myList[n]

fib(8)
print myList


myList = [0,1]
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 44, 65
def fib(n):
	if n < 1:
		return 'not a valid number in the sequence'
	l = len(myList)
	if n <= l:
		return myList[n-1]
	retVal = fib(n-1) + fib(n-2)
	myList.append(retVal)
	return myList[n]

fib(10)
print myList


# dry run

fib(1): 0
fib(2): 1
fib(3): 1
fib(4): 2

#EX-10

def evenl(l):

	evenList = []
	for i in l:
		if i % 2 == 0:
			evenList.append(i)
	return evenList

print evenl([1,2,3,4,5,6,7,8,9,10])

'''find divisors
sum of divisor and dvide 2 = that given number'''

#EX-11

def perfect(n):

	l = []
	sum = 0
	for i in range(1,n):
		if n % i == 0:
			l.append(i)
	for i in l:
		sum = sum + i
	if sum == n:
		return "perfect number"
	return "not perfect number"

print perfect(6)
print perfect(28)
print perfect(10)
print perfect(100)
print perfect(128)


#EX-12

'''palindrome
string = revstring then palindrome'''

def palin(s):

	revS = ''
	l = len(s)
	for i in range(1,l+1):
		revS = revS + s[-i]
	if revS == s:
		return "palindrome"
	return "not palindrome"

print palin("akash")
print palin("akashhsaka")

def palin1(s):
	for i in range(1,len(s)):
		if s[i] == s[-i]:
			return "palindrome"
	return "not palindrome"

print palin("akash")
print palin("akashhsaka")

#ex-14

import timeit


def pangram():
	l = "The quick brown fox jumps over the lazy dog The quick brown fox jumps over the lazy dog The quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dog"
	l1 = "abcdefghijklmnopqrstuvwxyz"
	for i in l1:
		if i not in l:
			return "not pangram"
	return "pangram"

print timeit.timeit(pangram)


def panagram2():
	l = "The quick brown fox jumps over the lazy dog The quick brown fox jumps over the lazy dog The quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dogThe quick brown fox jumps over the lazy dog"
	d = {}
	l = l.lower()
	#print dir(l)
	for c in l:
		if c.isalpha() and c not in d:
			d[c] = 0
	if len(d.keys()) == 26:
		return 'panagram'

print timeit.timeit(panagram2)


#ex-15

def hyphen(s):

	l = s.split("-")
	l.sort()
	print "-".join(l)
	'''s = ""

	
	for e in l:
		s = s + '-' + e
	print s[1:]
	lenght = len(l)
	for i in range(1,(2*lenght)-1):
		if i % 2 != 0:
			l.insert(i,"-")
	s1 = ''.join(l)
	return s1'''

print hyphen("akash-gandhi-dev")
print hyphen("green-red-yellow-black-white")
print hyphen("green-red-yellow-black-white-green-red-yellow-black-white-green-red-yellow-black-white-green-red-yellow-black-white-green-red-yellow-black-white")

#ex-16

def square():
	n = list(range(1,31))
	l = []
	for i in n:
		k = i*i
		l.append(k)
	print n
	return l

print square()


def pascal_triangle(n):
   trow = [1]
   y = [0]
   for x in range(max(n,0)):
      print(trow)
      trow=[l+r for l,r in zip(trow+y, y+trow)]
   return n>=1
pascal_triangle(6)



def pascal(n):
	r = [1]
	for x in range(n):
		print(r)
		r1 = r + [0]
		r2 = [0] + r
		r = []
		for i in range(len(r1)):
			r.append(r1[i] + r2[i])

pascal(9)





[1]
[1, 0] [0, 1] [1, 1]


[1, 1, 0] [0, 1, 1]  

for l, r in [ (1, 0), (1, 1), (0, 1)  ]:
	l = 1 r =1
	trow.append(l+r)

[1, 2, 1, 0]


print [x*x for x in range(1, 31)]

#max_of_three

def max3(a,b,c):

	if a > b:
		i = max(a,c)
		return i
	else:
		i = max(b,c)
		return i

print max3(5,10,15)


def max_of_two (a,b):
	if a > b:
		return a
	else:
		return b

def max_of_three(a,b,c):
	return max_of_two(c,max_of_two(a,b))

print max_of_three(5,10,7)



#len of string
def lenghtS(s):
	count = 0
	for i in s:
		count += 1
	return count

print lenghtS("akash")

#check vowel or not

def vowel(s):

	if s[0] in ("a,e,i,o,u"):
		return True
	else:
		return False

print vowel("mahesh")

#Write a function translate() that will translate a text into "rovarspraket" (Swedish for "robber's language"). That is, double every consonant and place an occurrence of "o" in between. For example, translate("this is fun") should return the string "tothohisos isos fofunon".
def trans(s):

	myString = ""
	for i in s:
		if i.lower() in "aeiou":
			myString = myString + (i + "o")
			
		elif i.lower() in "bcdfghjklmnpqrstvwxyz":
			
			myString = myString + (i + "o")*2
		elif i == " ":
			myString += " "
		else:
			pass
	return myString
			
		
print trans("Akash gandhi")

#Write a function is_member() that takes a value (i.e. a number, string, etc) x and a list of values a, and returns True if x is a member of a, False otherwise. (Note that this is exactly what the in operator does, but for the sake of the exercise you should pretend Python did not have this operator.)


def member(l, g):
	
	for i in l:
		if i == g:
			return True
	return False
	

print member(["akash", "gandhi", 2], 2)


#Define a function overlapping() that takes two lists and returns True if they have at least one member in common, False otherwise. You may use your is_member() function, or the in operator, but for the sake of the exercise, you should (also) write it using two nested for-loops

def overlapping(l1, l2):
	for i in l1:
		for x in l2:
			if x == i:
				return True
	return False

print overlapping(["akash", "gandhi"], [1, 2, 3, 4])

#Define a procedure histogram() that takes a list of integers and prints a histogram to the screen. For example, histogram([4, 9, 7]) should print the following:

'''****
*********
*******'''

def histogram(l):
	
	for i in l:
		print "*" * i

histogram([4,3,1])

#Write a program that maps a list of words into a list of integers representing the lengths of the correponding words

def WordToInt(l):
	lenght = len(l)
	count = 0
	
	l1 = []
	for i in range(0, lenght):		
		s = ''.join(l[i])
		
		for i in range(1,len(s)):
			count +=  i
	l1.append(count)	
	return l1

print WordToInt(["akash"])

def word(l):
	'''l1 = []
	for i in l:
		length = len(i)
		l1.append(length)

	return l1'''
	print [len(i) for i in l]

word(["akash"])


#Write a function find_longest_word() that takes a list of words and returns the length of the longest one.

def find_longest_word(l):
	l1 = []
	for i in l:
		line = len(i)
		l1.append(line)
	l1.sort()
	return l1[0]
	

print find_longest_word(["akash", "gandhi"])



#with word previous one.
def long(l):
	large = 0
	for i in l:
		if len(i) > large:
			large= len(i)
			largest_word = i

	print ("the longest word", largest_word , "and lenght", large)

long(["akash", "gandhi"])

#Write a function filter_long_words() that takes a list of words and an integer n and returns the list of words that are longer than n.


def flw(l, n):
	l1 = []
	for i in l:
		if len(i) > n:
			l1.append(i)
	return l1				 
	
	
	

print flw(["akash", "gandhi"], 5)

#The function max() from exercise 1) and the function max_of_three() from exercise 2) will only work for two and three numbers, respectively. But suppose we have a much larger number of numbers, or suppose we cannot tell in advance how many they are? Write a function max_in_list() that takes a list of numbers and returns the largest one.

'''def max(l):
	length = len(l)
	for i in range(1,length):
		if l[i] >= l[i+1]: #and l[i] >= l[:-i]:
			print l[i]
		else:
			pass
	length = len(l)
	for i in l:
		for x in range(1,length):
			if i > range(l[x],l[-1]):
				return i
			

print max([0,1,15,20,4,5])
'''

def maxInList(l):
	l.sort()
	return l[-1]

print maxInList([5,10,15,20,22,4])


#Write a version of a palindrome recognizer that also accepts phrase palindromes such as "Go hang a salami I'm a lasagna hog.", "Was it a rat I saw?", "Step on no pets", "Sit on a potato pan, Otis", "Lisa Bonet ate no basil", "Satan, oscillate my metallic sonatas", "I roamed under it as a tired nude Maori", "Rise to vote sir", or the exclamation "Dammit, I'm mad!". Note that punctuation, capitalization, and spacing are usually ignored.

def palin(s):
	s = s.lower()
	for x in s:
		if x not in "abcdefghijklmnopqrstuvwxyz":
			s = s.replace(x, '')
	print s
			
	for i in range(1,len(s)+1):
		if s[i-1] != s[-i]:
			return False
		
	return True

print palin("Go hang a salami I'm a lasagna hog.")



#A pangram is a sentence that contains all the letters of the English alphabet at least once, for example: The quick brown fox jumps over the lazy dog. Your task here is to write a function to check a sentence to see if it is a pangram or not.


def pangram(s):
	l = "abcdefghijklmnopqrstuvwxyz"
	for i in l:
		if i not in s:
			return False
	return True

print pangram("The quick brown fox jumps over the lazy dog.")


def pangram(s):
	d = {}
	s = s.lower()
	for i in s:
		if i.isalpha() and i not in d:
			d[i] = 0
	if len(d.keys()) == 26:
		return True
	return False

print pangram("The quick brown fox jumps over the lazy dog.")

'''"99 Bottles of Beer" is a traditional song in the United States and Canada. It is popular to sing on long trips, as it has a very repetitive format which is easy to memorize, and can take a long time to sing. The song's simple lyrics are as follows:

99 bottles of beer on the wall, 99 bottles of beer.
Take one down, pass it around, 98 bottles of beer on the wall.

The same verse is repeated, each time with one fewer bottle. The song is completed when the singer or singers reach zero.

Your task here is write a Python program capable of generating all the verses of the song.'''

n = 99
def load():

	n = 99
	for i in range(0,99):
		print ("%s bottles of beer on the wall, %s bottles of beer.\nTake one down, pass it around, %s bottles of beer on the wall." %(n,n,n-1))
		n -= 1

load()


#Write a function char_freq() that takes a string and builds a frequency listing of the characters contained in it. Represent the frequency listing as a Python dictionary. Try it with something like char_freq("abbabcbdbabdbdbabababcbcbab").



def freq(s):
	
	s = s.lower()
	d = {}
	count = 0
	for i in s:
		if i.isalpha() and i not in d:
			d[i] = 1
		elif i.isalpha() and i in d:
			d[i] += 1
		
	
	print d.keys()
	print d.values()
	print len(d.keys())
	return d

print freq("abbabcbdbabdbdbabababcbcbab")


'''In cryptography, a Caesar cipher is a very simple encryption techniques in which each letter in the plain text is replaced by a letter some fixed number of positions down the alphabet. For example, with a shift of 3, A would be replaced by D, B would become E, and so on. The method is named after Julius Caesar, who used it to communicate with his generals. ROT-13 ("rotate by 13 places") is a widely used example of a Caesar cipher where the shift is 13. In Python, the key for ROT-13 may be represented by means of the following dictionary:

key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 
       'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c', 
       'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k',
       'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S', 
       'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A', 
       'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I', 
       'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}
Your task in this exercise is to implement an encoder/decoder of ROT-13. Once you're done, you will be able to read the following secret message:

   Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!
Note that since English has 26 characters, your ROT-13 program will be able to both encode and decode texts written in English.'''

def rot_13(s):
	key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 
       'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c', 
       'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k',
       'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S', 
       'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A', 
       'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I', 
       'W':'J', 'X':'K', 'Y':'L', 'Z':'M', ' ': ' ', '?':'?', '!':'!'}
	s = s.lower()
	s1 = ""
	for i in s:
		#if i.isalpha():
		i = key[i]
		s1 += i
	return s1

print rot_13("Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!")

#Define a simple "spelling correction" function correct() that takes a string and sees to it that 1) two or more occurrences of the space character is compressed into one, and 2) inserts an extra space after a period if the period is directly followed by a letter. E.g. correct("This   is  very funny  and    cool.Indeed!") should return "This is very funny and cool. Indeed!" Tip: Use regular expressions!


'''The third person singular verb form in English is distinguished by the suffix -s, which is added to the stem of the infinitive form: run -> runs. A simple set of rules can be given as follows:

If the verb ends in y, remove it and add ies
If the verb ends in o, ch, s, sh, x or z, add es
By default just add s
Your task in this exercise is to define a function make_3sg_form() which given a verb in infinitive form returns its third person singular form. Test your function with words like try, brush, run and fix. Note however that the rules must be regarded as heuristic, in the sense that you must not expect them to work for all cases. Tip: Check out the string method endswith().'''

def third(s):
	

	if s.endswith("y"):
		s1 = s[:-1]
		s1 = s1 + "ies"
		return s1
	
	elif s.endswith("o") or s.endswith("s") or s.endswith("x") or s.endswith("z"):
		
		s = s + "es"
		return s
	
	elif s.endswith("ch") or s.endswith("sh"):
		
		s = s + "es"
		return s
	
	else:
		s = s + "s"
		return s
print third("play")
print third("brush")
print third("run")
print third("fix")
print third("help")

'''In English, the present participle is formed by adding the suffix -ing to the infinite form: go -> going. A simple set of heuristic rules can be given as follows:

If the verb ends in e, drop the e and add ing (if not exception: be, see, flee, knee, etc.)
If the verb ends in ie, change ie to y and add ing
For words consisting of consonant-vowel-consonant, double the final letter before adding ing
By default just add ing
Your task in this exercise is to define a function make_ing_form() which given a verb in infinitive form returns its present participle form. Test your function with words such as lie, see, move and hug. However, you must not expect such simple rules to work for all cases.'''


		
	

def ing(s):
	l1 = "aeiou"
	
	if s.endswith("ie"):
		
		
		return s[:-2] + "ying"


	elif s.endswith("e") and s != "be" and s != "see" and s != "flee" and s != "knee":
		
		return s[:-1] + "ing"
	
		
	elif s[-1] not in l1 and s[-2] in l1 and s[-3] not in l1:
		
	
		return s + s[-1] + "ing"
	
	else:
	
		return s + "ing"
		
print ing('be')
print ing('lie')
print ing('see')
print ing('move')
print ing('hug')
print ing("be")
print ing("stop")
print ing("play")

#Write a program that maps a list of words into a list of integers representing the lengths of the correponding words. Write it in three different ways: 1) using a for-loop, 2) using the higher order function map(), and 3) using list comprehensions.

def lens(l):
	s = ""
	l2 = []
	for i in l:
		s = i
		l1 = len(s)
		l2.append(l1)
	return l2
	
print lens(["akash","gandhi"])

l = ["akash","gandhi"]
print [len(i) for i in l]

print map(lambda x:len(x),l)

def myFunc(f):
	f = [1]
	return f
		
g = [0], {0: 1}, (0)
g = myFunc(g)
what will be value of g?

#Using the higher order function reduce(), write a function max_in_list() that takes a list of numbers and returns the largest one. Then ask yourself: why define and call a new function, when I can just as well call the reduce() function directly?

print reduce(lambda x,y: x if (x>y) else y,[1,2,3,100,3,2,10])

#Write a function find_longest_word() that takes a list of words and returns the length of the longest one. Use only higher order functions.

print max(map(len,["akash","gandhi","devanshi"]))

#print reduce(lambda x,y : x if x>y else y, ["gandhi","devanshi"])

#print filter(lambda x,y : len(x)>len(y), ["akash","gandhi","devanshi"])

print [max(len(i) for i in ["akash","gandhi","devanshi"])]


#Using the higher order function filter(), define a function filter_long_words() that takes a list of words and an integer n and returns the list of words that are longer than n.

print filter(lambda x,n=10: len(x)>n,["aaaaaaaaaaaa","abd","bbbbbbbbbbbbbbbb"])

#Represent a small bilingual lexicon as a Python dictionary in the following fashion {"merry":"god", "christmas":"jul", "and":"och", "happy":gott", "new":"nytt", "year":"r"} and use it to translate your Christmas cards from English into Swedish. Use the higher order function map() to write a function translate() that takes a list of English words and returns a list of Swedish words.

'''def translate(l1):

	l = ["god","jul","och","gott","nytt","ar"]

	for i in range(0,len(l1)):
		l1[i] = l[i]
	return l1

print translate(["merry"])

import sys
def translate(words):
    lexicon = {"merry": "god", "christmas": "jul", "and": "och", "happy": "gott", "new": "nytt", "year": "ar"}
    return map(lambda word: lexicon[word], words)

if __name__ == "__main__":
    print translate(["merry", "christmas"])'''


def trans():

	d =  {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"}
	return map(lambda x : d[x], ["merry"])

#Write a version of a palindrome recogniser that accepts a file name from the user, reads each line, and prints the line to the screen if it is a palindrome.

'''def palindrome(s):

	
	for i in range(1,len(s)+1):
		print s[i-1]
		print s[-i]
		if s[i-1] != s[-i]:
		
			return "False"
	return "True"

print palindrome("abbaa")'''
import os	

'''def palindrome_io(file_, mode):
    stuff = "`~!@#$%^&*()_-=+[]{}\|;:,<.>/?"
    with open(file_, mode) as f:
        for line in f:
            for char in line:
                if char in stuff:
                    line = line.replace(char, "")
            if line.lower().strip() == line[::-1].lower().strip():
                print True
            else:
                print False
palindrome_io(r'/home/akashgandhi10/Documents/file.txt', 'r+')


def palindrome_io(file_, mode):
    with open(file_, mode) as f:
        for line in f:
            line = line.translate(None, "`~!@#$%^&*()_-=+[]{}\|;:,<.>/?").lower().strip()
            print str(line == line[::-1])

palindrome_io(r'C:\Users\Brian Gunsel\Desktop\test.txt', 'r+')'''

def palindrome_io(file,mode):
	f = open(file, 'r+')
	for l in f.readlines():
		l = l.translate(None,"!@#$%^&*(){}_+<>?,./;:[]-=").lower().strip()
		
		if l == l[::-1]:	
			print l

palindrome_io('/home/akashgandhi10/Documents/text.txt', 'r+')

#According to Wikipedia, a semordnilap is a word or phrase that spells a different word or phrase backwards. ("Semordnilap" is itself "palindromes" spelled backwards.) Write a semordnilap recogniser that accepts a file name (pointing to a list of words) from the user and finds and prints all pairs of words that are semordnilaps to the screen. For example, if "stressed" and "desserts" is part of the word list, the the output should include the pair "stressed desserts". Note, by the way, that each pair by itself forms a palindrome!




def palindrome_io(file,mode):
	f = open(file, 'r+')
	for l in f.readlines():
		l = l.translate(None,"!@#$%^&*(){}_+<>?,./;:[]-=").lower().strip()
		
		if l == l[::-1]:	
			print l

palindrome_io('/home/akashgandhi10/Documents/text.txt', 'r+')

#Write a procedure char_freq_table() that, when run in a terminal, accepts a file name from the user, builds a frequency listing of the characters contained in the file, and prints a sorted and nicely formatted character frequency table to the screen.

def freq_io(file):
	f = open(file,"r+")	
	d = {}
	for l in f:
		for char in l:
			if char not in d:
				d[char] = 0
			d[char] += 1
	print d

if __name__ == "__main__":
	freq_io("/home/akashgandhi10/Documents/text.txt")



The International Civil Aviation Organization (ICAO) alphabet assigns code words to the letters of the English alphabet acrophonically (Alfa for A, Bravo for B, etc.) so that critical combinations of letters (and numbers) can be pronounced and understood by those who transmit and receive voice messages by radio or telephone regardless of their native language, especially when the safety of navigation or persons is essential. Here is a Python dictionary covering one version of the ICAO alphabet:

d = {'a':'alfa', 'b':'bravo', 'c':'charlie', 'd':'delta', 'e':'echo', 'f':'foxtrot',
     'g':'golf', 'h':'hotel', 'i':'india', 'j':'juliett', 'k':'kilo', 'l':'lima',
     'm':'mike', 'n':'november', 'o':'oscar', 'p':'papa', 'q':'quebec', 'r':'romeo',
     's':'sierra', 't':'tango', 'u':'uniform', 'v':'victor', 'w':'whiskey', 
     'x':'x-ray', 'y':'yankee', 'z':'zulu'}
Your task in this exercise is to write a procedure speak_ICAO() able to translate any text (i.e. any string) into spoken ICAO words. You need to import at least two libraries: os and time. On a mac, you have access to the system TTS (Text-To-Speech) as follows: os.system('say ' + msg), where msg is the string to be spoken. (Under UNIX/Linux and Windows, something similar might exist.) Apart from the text to be spoken, your procedure also needs to accept two additional parameters: a float indicating the length of the pause between each spoken ICAO word, and a float indicating the length of the pause between each word spoken.'''

from gtts import gTTS
import os
tts = gTTS(text='Good morning', lang='en')
tts.save("good.mp3")
#os.system("mpg321 good.mp3")



from gtts import gTTS
from tempfile import TemporaryFile
tts = gTTS(text='Hello', lang='en')
f = TemporaryFile()
tts.write_to_fp(f)
f.close()
def ICAO(file):
	f = open(file,"r+")
	d = {'a':'alfa', 'b':'bravo', 'c':'charlie', 'd':'delta', 'e':'echo', 'f':'foxtrot',
     'g':'golf', 'h':'hotel', 'i':'india', 'j':'juliett', 'k':'kilo', 'l':'lima',
     'm':'mike', 'n':'november', 'o':'oscar', 'p':'papa', 'q':'quebec', 'r':'romeo',
     's':'sierra', 't':'tango', 'u':'uniform', 'v':'victor', 'w':'whiskey', 
     'x':'x-ray', 'y':'yankee', 'z':'zulu'}
	
	os.system("akash")
	for l in f.readlines():	
		l = l.lower().strip()
		for char in l:
			if char == ' ':
				pass
			else:
				
				
				print (char + " as in " + d[char])
	
	

if __name__ == "__main__":
	ICAO("/home/akashgandhi10/Documents/text.txt")

# 36 35 and map reduce filter

#Write a program that given a text file will create a new text file in which all the lines from the original file are numbered from 1 to n (where n is the number of lines in the file).

def copy(file, file1):

	f = open(file,"r+")
	f1 = open(file1, "w+")
	'''print f.read()
	f.seek(0,0)
	print f.readline()
	f.seek(0,0)
	print f.readlines()
	f.seek(0,0)'''
	n =1
	for l in f.readlines():
		f1.write(str(n) + ": " + l)
		n += 1
	f.close()
	f1.close()
	
	
if __name__ == "__main__":
	copy("/home/akashgandhi10/Documents/text.txt", "/home/akashgandhi10/Documents/text1.txt")

#Write a program that will calculate the average word length of a text stored in a file (i.e the sum of all the lengths of the word tokens in the text, divided by the number of word tokens).

def avg(file):
	f = open(file, "r+")
	numberOfWords = 0
	sumOfLengths = 0.0
	for l in f.readlines():
		numberOfWords = numberOfWords + len(l.split(" "))
		l = l.replace(" ","")
		sumOfLengths += len(l)
		
	average = 0
	
	average = sumOfLengths/numberOfWords
	print average
	f.close()

if __name__ == "__main__":
	avg("/home/akashgandhi10/Documents/text.txt")

#A hapax legomenon (often abbreviated to hapax) is a word which occurs only once in either the written record of a language, the works of an author, or in a single text. Define a function that given the file name of a text will return all its hapaxes. Make sure your program ignores capitalization.

def hapax(file):

	f = open(file, "r+")
	d = {}
	for l in f.readlines():
		
		l = l.lower().strip().split(" ")
		
		for j in l:
		
			if j not in d:
				d[j] = 1
			else:
				d[j] = d[j] + 1
			

	
	
		
	
	for i in d:
		if d[i] == 1:
			print ("hapax is :" + i)

if __name__ == "__main__":
	hapax('/home/akashgandhi10/Documents/text.txt')

#Write a program able to play the "Guess the number"-game, where the number to be guessed is randomly chosen between 1 and 20. (Source: http://inventwithpython.com) This is how it should work when run in a terminal:

'''>>> import guess_number
Hello! What is your name?
Torbjorn
Well, Torbjrn, I am thinking of a number between 1 and 20.
Take a guess.
10
Your guess is too low.
Take a guess.
15
Your guess is too low.
Take a guess.
18
Good job, Torbjrn! You guessed my number in 3 guesses!'''


def guess(file):
	f = open(file, "r+")
	
	name = input("Hello! what is your name?\n")
	print("Well, " + name + ", I am thinking of a number between 1 and 20.")
	count = 0
	i = f.readline()
	j = 1

	
	while j:
		count += 1
		number = input("Take a guess.\n")
		i = int(i)
		if i == number:
			print ("Good job, " + name + "! You guessed my number in " + str(count) + " guesses!'''")
			break
		elif i > number:
			print ("Your guess is too low")
			
		
		elif i < number:
			print("Your guess is too high")
		j += 1
	
		
		
if __name__ == "__main__":
	guess('/home/akashgandhi10/Documents/text.txt')

import sys 

text = ""
while 1:
   c = sys.stdin.read(1)
   text = text + c
   if c == '\n':
       break

print("Input: %s" % text)"""

import random
n = 20
to_be_guessed = int(n * random.random()) + 1
guess = 0
while guess != to_be_guessed:
    guess = int(input("New number: "))
    if guess > 0:
        if guess > to_be_guessed:
            print("Number too large")
        elif guess < to_be_guessed:
            print("Number too small")
    else:
        print("Sorry that you're giving up!")
        break
else:
    print("Congratulation. You made it!")
		

	
	








































		





































































































	
	
			

















































