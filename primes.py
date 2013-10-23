def primes(n):
    """
    a python implementation of the Eratothenes Sieve 
    """
    sqrtN=n**0.5
    odds=[2]
    odds+=[i for i in range(3,n) if i%2>0]

    for i in odds:
        if i!=0 and i<=sqrtN:
            for j in odds[odds.index(i)+1:]:
                if j%i==0:
                    odds[odds.index(j)]=0
    return [i for i in odds if i!=0]
