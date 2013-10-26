import itertools

c=itertools.cycle([1,2,3,4])
clist=[c.__next__() for i in range(9)]

"""
>>> clist
[1, 2, 3, 4, 1, 2, 3, 4, 1]
"""
