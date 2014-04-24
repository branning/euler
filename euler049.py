#!/usr/bin/env python

from euler007 import eratosthenes
import itertools

# all primes with 4 digits
primes = eratosthenes(10000)
primes = filter(lambda a: a>999, primes)
primes_set = set(primes)

perm_sets = []
for p in primes:
  if perm_sets and p in reduce(set.union, perm_sets[:]):
    continue
  perm_set = set((p,))
  for perm in itertools.permutations(str(p)):
    perm = int(''.join(perm))
    if perm in primes_set:
      perm_set.add(perm)
  if len(perm_set) > 2:
    perm_sets.append(perm_set)

def deltas(array):
  d = []
  for i in range(len(array) - 1):
    d.append(array[i+1]-array[i])
  return d

example = (1487, 4817, 8147)

perm_lists = [list(p) for p in perm_sets]
#map(list.sort, perm_lists)
for perm_list in perm_lists:
  for combo3 in itertools.combinations(perm_list, 3):
    if combo3[1]-combo3[0] == combo3[2] - combo3[1] \
      and combo3 != example:
      #print "Arithmetic sequence of {} in {}".format(combo3[1]-combo3[0], combo3)
      print ''.join([str(c) for c in combo3])
