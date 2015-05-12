def sieve(n): #Sieve of Eratosthenese
	np1 = n + 1
	s = list(range(np1))
	s[1] = 0
	#only need to look up to sqrt(n) for sieve to remove multiples
	sqrtn = int(round(n**0.5))
	for i in range(2, sqrtn + 1):
    	if s[i]:
        	#remove multiples of non-primes:
        	s[i*i: np1: i] = [0] * len(range(i*i, np1, i))
	#return list of primes, without repeating 0's
	return filter(None, s)

print sum(sieve(2000000))