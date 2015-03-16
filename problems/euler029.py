#!/usr/bin/env python

terms = set()
maxA = 100
maxB = 100
for a in range(2,maxA+1):
  for b in range(2,maxB+1):
    value = a**b
    if value not in terms:
      terms.add(value)

debugging = False
if debugging:
  a = list(terms)
  a.sort()
  print a
print len(terms)
