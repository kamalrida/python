[i%2 for i in range(10)]
[i for i in range(10) if i%2]
[j**2 for j in [i for i in range(10) if i%2] if j>2]
[i**2 for i in range(10) if i%2 if i>2] ## same as previous
