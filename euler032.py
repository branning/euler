#!/usr/bin/env python

import itertools

pandigital_products = set()

for a in range(2,100):
    a_set = set(list(str(a)))
    if '0' in a_set: # zeros not allowed
        continue
    if len(a_set) != len(str(a)): # no duplicate digits allowed
        continue
    nums = set(map(str, range(1,10))) # all digits 1-9
    nums -= a_set
    for b_set in itertools.combinations(nums, 5-len(a_set)): # 3 digit numbers
        left = nums - set(b_set)
        for b_str in itertools.permutations(b_set):
            b = int(''.join(b_str))
            product = a*b
            if len(str(product)) + len(str(a)) + len(b_str) != 9: # too few/many digits
                continue
            product_set = set(list(str(product)))
            if '0' in product_set: # no zeros allowed
                continue
            if len(product_set) < len(str(product)): # duplicates not allowed
                continue
            if not left.issuperset(product_set):
                continue
            left = left - product_set                
            if left == set(): # set() is empty set
                #print "Pandigital product: {} * {} = {}".format(a, b, product)
                pandigital_products.add(product)

#print sorted(list(pandigital_products))
print sum(pandigital_products)