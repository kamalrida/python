import itertools

c=itertools.cycle([1,2,3,4])
[c.__next__() for i in range(9)]
