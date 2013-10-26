nums=[127,755,1407,2134]
keys=[815031,137335,636456,933782]

list(map(lambda x:x*2, nums))
"""
>>> list(map(lambda x:x*2, nums))
[254, 1510, 2814, 4268]
"""
list(map(lambda i,j:i-j,keys,nums))
"""
>>> list(map(lambda i,j:i-j,keys,nums))
[814904, 136580, 635049, 931648]
"""
