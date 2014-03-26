#!/usr/bin/env python

from euler007 import eratosthenes
import itertools
from collections import deque

limit = 10**6
primes = set(eratosthenes(limit))

debugging = False

circular_primes = set()
for n in range(2, limit):
	duplicate = False
	n_str = deque(str(n))
	for i in range(len(n_str)):
		if int(''.join(n_str)) in circular_primes:
			duplicate = True
			break
		n_str.rotate(1)
	if duplicate:
		continue
	circular = True
	for i in range(len(n_str)):
		if not int(''.join(n_str)) in primes:
			circular = False
			break
		n_str.rotate(1)
	if circular:
		for i in range(len(n_str)):			
			if debugging:
				print "Circular prime: {}".format(''.join(n_str))
			circular_primes.add(int(''.join(n_str)))
			n_str.rotate(1)

if debugging:
	print circular_primes
	print "found {} circular primes".format(len(circular_primes))
else:
	print len(circular_primes)