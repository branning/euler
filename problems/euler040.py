#!/usr/bin/env python

limit = 10**6
digits = []
counter = 0
while len(digits) < limit:
  counter += 1
  digits.extend(list(str(counter)))

selected = [10**i for i in range(7)]
d = []
for s in selected:
  d.append(int(digits[s-1]))

print reduce(lambda x,y: x*y, d)
