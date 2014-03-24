#!/usr/bin/env python

from operator import mul
from euler012 import prime_factorize

def reduce_fraction(num,den):
	# factorize numerator and denominator
	num_factors = prime_factorize(num)
	den_factors = prime_factorize(den)

	# find the greatest common factor of the numerator and denominator
	greatest_factor = 1
	for f in den_factors:
		if f in num_factors:
			greatest_factor *= f**min(den_factors[f], num_factors[f])

	return (num/greatest_factor,den/greatest_factor)

fractions = {}

debugging = False
for num in range(10,100):
	for den in range(num,100):
		# skip 1's
		if num == den:
			continue
		num_str = str(num)
		den_str = str(den)
		# skip trivial examples with cancelable zeros
		if '0' == num_str[1] == den_str[1]:
			continue
		for a,b in [(a,b) for a in [0,1] for b in[0,1]]:
			if int(den_str[b]) == 0:
				continue
			# misleading cancellable fractions: ab / cd = one of a/c,a/d,b/c,b/d 
			# and the cancelled digits are the same, e.g. ab/cd = a/d, b=c. 49/98 = 4/8,9=9
			if 1.*num/den == 1.*int(num_str[a]) / int(den_str[b]) \
			    and num_str[(a+1)%2] == den_str[(b+1)%2]: # the cancelled chars are the same
				if debugging:
					print "{} / {} equals {} / {}".format(num,den,num_str[a],den_str[b])
				fractions[num,den] = (num_str[a],den_str[b])
				break

num = reduce(mul, [int(a) for a,b in fractions.values()])
den = reduce(mul, [int(b) for a,b in fractions.values()])
a,b = reduce_fraction(num,den)
print b