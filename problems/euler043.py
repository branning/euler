#!/usr/bin/env python

import re

debugging=False

# find all multiples of 2 with no repeat digits, including 0
mult = {}
wheels = [2,3,5,7,11,13,17]

for n in wheels:
  mult[n] = []
  for i in range(n, 1000, n):
    i_str = str(i).zfill(3)
    if len(i_str) == len(set(i_str)):
      mult[n].append(i_str)
  if debugging:
    print n, len(mult[n])

# for each number, make a set of the unique suffixes
# then remove from the succeeding set all numbers which have prefixes
# that are not among that set of suffixes
# e.g., there are 45 unique suffixes in the 3-digit, 2-divible numbers
# with no repeat digits.  Remove all teh 3-digit, 3-divisible numbers that
# do not start with one of those 2-digit suffixes

for pre,post in zip(wheels[:-1],wheels[1:]):
  suffixes = set([re.search('(.{2})$', i).group(1) for i in mult[pre]])
  to_remove = []
  for n in range(len(mult[post])):
    if mult[post][n][0:2] not in suffixes:
      to_remove.append(mult[post][n])
  for r in to_remove:
    mult[post].remove(r)
  if debugging:
    print post, len(mult[post])

for pre,post in zip(wheels[-2::-1], wheels[-1::-1]):
  prefixes = set([re.search('^(.{2})', i).group(1) for i in mult[post]])
  to_remove = []
  for n in range(len(mult[pre])):
    if mult[pre][n][1:3] not in prefixes:
      to_remove.append(mult[pre][n])
  for r in to_remove:
    mult[pre].remove(r)
  if debugging:
    print pre, len(mult[pre])

def join_partial(pre,post):
  partials = []
  for a in pre:
    for z in post:
      if a[-2:]==z[:2]:
        if set(a[:-2]).isdisjoint(set(z[2:])):
          partials.append(a+z[2:])
  return partials

pandigitals = mult[17]
for n in wheels[-2::-1]:
  pandigitals = join_partial(mult[n], pandigitals)

digits = set('0123456789')
for p in range(len(pandigitals)):
  pandigitals[p] = list(digits.symmetric_difference(set(pandigitals[p]))) + list(pandigitals[p])
  pandigitals[p] = int(''.join(pandigitals[p]))
if debugging:
  print pandigitals
print sum(pandigitals)
