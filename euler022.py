#!/usr/bin/env python

namefile = open('names.txt')

def namesum(name):
  capA = ord('A')
  return sum([ord(n)-capA+1 for n in name])

names = []
for lump in namefile.xreadlines():
  names.extend([name.strip('"') for name in lump.split(',')])

names.sort()
ord_pos_sum = 0
for i,n in enumerate(names):
  ord_pos_sum += (i+1) * namesum(n)

print ord_pos_sum
