#!/usr/bin/env python

from math import factorial

curious_numbers = []
facts = [factorial(i) for i in range(10)]
for i in range(3,100000):
	if sum([facts[int(d)] for d in str(i)]) == i:
		curious_numbers.append(i)
print sum(curious_numbers)
