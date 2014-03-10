#!/usr/bin/env python


firsts = [1]
jan = 31
mar_dec = [31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for year in range(1901,2001):
  firsts.append(firsts[-1] + jan)
  if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    feb = 29
  else:
    feb = 28
  firsts.append(firsts[-1] + feb)
  for mon in mar_dec:
    firsts.append(firsts[-1] + mon)

print sum([1 for i in firsts if i%7==6])
