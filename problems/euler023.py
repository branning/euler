#!/usr/bin/env python

from euler007 import eratosthenes
from euler012 import proper_divisors
from math import sqrt, ceil

def MakeAbundant(limit=28123):
  primes = eratosthenes(int(ceil(sqrt(limit))))
  abundant_numbers = set()
  for i in range(12,limit+1):
    if sum(proper_divisors(i, primes)) > i:
      abundant_numbers.add(i)
  return abundant_numbers

def MakeSum(n, numbers):
  a = 0
  b = len(numbers) - 1
  # Find a sensible starting point for b
  while numbers[a] + numbers[b] != n:
    while numbers[a] + numbers[b] > n:
      b -= 1
      if b < a:
        return None
    if numbers[a] + numbers[b] == n:
      return (numbers[a], numbers[b])
    else:
      while numbers[a] + numbers[b] < n:
        a += 1
        if a > b:
          return None
  else:
    return (numbers[a], numbers[b])

if __name__=="__main__":
  limit = 28123
  abundant_numbers = MakeAbundant(limit)
  abundant_list = list(abundant_numbers)
  nosum = []
  for i in range(1, limit):
    if MakeSum(i, abundant_list) is None:
      nosum.append(i)
  print sum(nosum)
