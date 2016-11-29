import timeit

def main():
    # print "10"
    # import pdb; pdb.set_trace()
    #for loop
    print timeit.timeit("'-'.join(str(n) for n in range(100))", number = 10000)
    #list comprehensive
    print timeit.timeit("'-'.join([str(n) for n in range(100)])", number = 10000)
    #map function
    print timeit.timeit("map(str, range(100))", number = 10000)

if __name__ == "__main__":
    main()
