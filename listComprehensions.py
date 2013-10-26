[i%2 for i in range(10)]
"""
>>> [i%2 for i in range(10)]
[0, 1, 0, 1, 0, 1, 0, 1, 0, 1]

"""

[i**.5 for i in range(10) if i%2]
"""
>>> [i**.5 for i in range(10) if i%2]
[1.0, 1.7320508075688772, 2.23606797749979, 2.6457513110645907, 3.0]
"""

[j**2 for j in [i for i in range(10) if i%2] if j>2]
"""
>>> [j**2 for j in [i for i in range(10) if i%2] if j>2]
[9, 25, 49, 81]
"""

[i**2 for i in range(10) if i%2 if i>2] ## same as previous
