#!/usr/bin/env python

from operator import mul

debugging = False
digits = set(range(1,10))

'''
import itertools
# first idea, all permutations of pandigital products, and find divisors
pandigital_products = []
for n in itertools.permutations(digits):
	for divisor in digits[2:]:
		if n % divisor != 0:
'''

limit = 10**4
pandigital_mult = {}

for i in range(2, limit):
	products = set() #
	multiple = 0
	while products != digits:
		multiple += 1
		product = i * multiple
		if len(str(product)) != len(set(str(product))): # duplicate
			break
		product_set = set([int(s) for s in str(product)])
		if not product_set.isdisjoint(products): # some digits already in product set
			break
		products.update(product_set)
	else: # found a pandigital set!
		pandigital_mult[i] = multiple

max_product = 0
for n in pandigital_mult:
	if debugging:
		print n, pandigital_mult[n], [n*i for i in range(1,pandigital_mult[n]+1)]
	product = int(reduce(lambda x,y: x+y, [str(n*i) for i in range(1,pandigital_mult[n]+1)]))
	if product > max_product:
		max_product = product

print max_product
