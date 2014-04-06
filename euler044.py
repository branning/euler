#!/usr/bin/env python

import math

def pentagon(n):
  return n*(3*n-1)/2
def inv_pentagon(n):
  return (1+math.sqrt(24*n+1)) % 6 == 0

if __name__=="__main__":
  pents = set()
  pent_pairs = []
  i = 0
  stop = False
  while not stop:
    i += 1
    next = pentagon(i)
    for p in pents:
      diff = next-p
      total = next+p
      if inv_pentagon(diff) and inv_pentagon(total):
        pent_pairs.append((next,p))
        stop = True
    pents.add(next)
    if i > 10000:
      break
  print min([a-b for a,b in pent_pairs])
