from collections import Counter

l = [1,1,1,2,2,3,3,3,1,2,3,4,5,4,4,4,5,5,6]
print Counter(l)

s = "akash gandhi aaaaaa bbb cc d akash gandhi"
print Counter(s)

word = s.split()
print s.split()
print Counter(word)

c = Counter(word)
print c.most_common(2)
print c.most_common(3)
print c.most_common()[:-1]
print c.most_common()[:-2:-1]
print c.most_common()[:-3:-1]
print c.most_common()[::-1]
print sum(c.values())

l = [1,1,1,2,2,3,3,3,1,2,3,4,5,4,4,4,5,5,6,0,-1,-1,0]
lc = Counter(l)
print sum(lc.values())
lc.clear()
print sum(lc.values())

lc = Counter(l)
print lc
print list(lc)
print set(lc)
print dict(lc)
print lc.items()
lcp = lc.items()
print Counter(dict(lcp))

l = [1,1,1,2,2,3,3,3,1,2,3,4,5,4,4,4,5,5,6,0,-1,-1,0]
x = Counter(l)
x += Counter(l)
print x
