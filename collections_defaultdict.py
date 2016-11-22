from collections import defaultdict

d = {}
# d["one"]

# d = {"a": 1}
# print d["a"]
#d["b"]

d = defaultdict(object)
print d["one"]
# print d.keys()
for item in d:
    print item

d = defaultdict(lambda: 0)
print d["one"]
d["two"] = 2
print d["two"]
print d

# d = defaultdict()
# print d["one"]
# d["two"] = 2
# print d["two"]
# print d
