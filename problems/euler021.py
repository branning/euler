#!/usr/bin/env python

from euler007 import eratosthenes
from euler012 import proper_divisors

debugging = False

limit = 10000
sums_of_divisors = {}
amicable_numbers = set()
primes = set(eratosthenes(limit))
for n in xrange(6, limit):
  sod = sum(proper_divisors(n, primes))
  sums_of_divisors[n] = sod
  if sod != n and sod in sums_of_divisors.keys() and sums_of_divisors[sod] == n:
    # found amicable numbers!
    amicable_numbers.add((n, sod))

if debugging:
  print amicable_numbers

soan = 0
for pair in amicable_numbers:
  soan += sum(pair)

print soan
