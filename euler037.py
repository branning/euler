#!/usr/bin/env python

from euler007 import eratosthenes

debugging = False

# they don't give us hints about the limit ..?
limit = 10**6
primes = eratosthenes(limit)
prime_set = set(primes)

truncatable_primes = []
for p in primes[4:]: # skip 2,3,5,7
	p_str = list(str(p))
	for i in range(len(p_str) - 1):
		del(p_str[0]) # truncate from the left
		if int(''.join(p_str)) not in prime_set:
			break # not truncatable
	else:
		p_str = list(str(p))
		for i in range(len(p_str) - 1):
			del(p_str[-1]) # truncate from the right
			if int(''.join(p_str)) not in prime_set:
				break # not truncatable		
		else:
			if debugging:
				print p,
			truncatable_primes.append(p)

if debugging:
	print "Found {} truncatable primes: {}".format(len(truncatable_primes), 
		truncatable_primes)
print sum(truncatable_primes)