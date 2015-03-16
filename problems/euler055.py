#!/usr/bin/env python

from euler004 import analytical_reverse, isPalindrome

lychrel = []

for n in range(1,10000):
  process = n
  for i in range(50):
    process += analytical_reverse(process)
    if isPalindrome(process):
      break
  else:
    lychrel.append(n)
print len(lychrel)
