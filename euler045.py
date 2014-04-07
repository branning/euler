#!/usr/bin/env python

import math

def triangle(n):
  return n*(n+1)/2

def in_pentagon(n):
  return (1 + math.sqrt(24*n+1)) % 6 == 0
def in_hexagon(n):
  return (1 + math.sqrt(8*n+1)) % 4 == 0

# the example point is triangle(285)==pentagon(165)==hexagon(143)
n = 285
limit = 1000000 # don't run forever..
while n<limit:
  n += 1
  t_n = triangle(n)
  if in_pentagon(t_n) and in_hexagon(t_n):
    print t_n
    break
else:
  print "Failed to find intersecting triangle, pentagonal, hexagonal under {}".format(limit)
