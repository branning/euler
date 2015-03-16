#!/usr/bin/env python

def quinticsum(x):
  s = 0
  while x>0:
    s += (x % 10)**5
    x /= 10
  return s

debugging = False
sumisn = []
for n in range(10,1000000):
  s = quinticsum(n)
  if n==s:
    if debugging:
      print "quinctic sum of digits of {} is {}".format(n,s)
    sumisn.append((n,s))
print sum([s for n,s in sumisn])
