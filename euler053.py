#!/usr/bin/env python

from math import factorial

facts = [factorial(i) for i in xrange(101)]

def combination_count(n,r, facts):
  return facts[n]/(facts[r]*facts[n-r])

gt_million = 0
for n in xrange(1,101):
  for r in xrange(1,n+1): # r <= n
    if combination_count(n,r,facts) > 10**6:
      gt_million += 1
print gt_million
