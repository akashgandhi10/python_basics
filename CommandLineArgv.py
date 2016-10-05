import sys

def main1(a, b, c):
	print a + b + c
	func2()
	infc3()
	func4()
	return 'bullshit'


if __name__ == "__main__":
	print sys.argv
	print len(sys.argv)
	a = int(sys.argv[1])
	b = int(sys.argv[2])
	c = int(sys.argv[3])
	main(a, b, c)
	func1()
	func2()
	func3()
	finc4()
