from collections import Counter

l = [1,1,1,2,2,3,3,3,1,2,3,4,5,4,4,4,5,5,6]
print Counter(l)

s = "akash gandhi aaaaaa bbb cc d akash gandhi"
print Counter(s)

word = s.split()
print Counter(word)

c = Counter(word)
print c.most_common(2)
print c.most_common(3)
