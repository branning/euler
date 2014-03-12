#!/usr/bin/env python

from euler007 import eratosthenes

primes = eratosthenes(2000000)
print sum(primes)
