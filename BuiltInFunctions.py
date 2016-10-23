print map(len , "akash gandhi".split())

print reduce(lambda x,y: x* 10 + y, [3,4,5])

print filter(lambda x: x.startswith("a"),["akash","gandhi","aa","abc","cd","bc"])

print [x +"-"+y for x,y in zip(["A","b"],["B","a"])]

print {j:i  for i,j in enumerate(["a", "b", "c"])}

# print map(lambda x,y: x and y, enumerate(["a", "b", "c"])

print [j for i,j in enumerate([0,1,1,2,4,4,6]) if i==j]
