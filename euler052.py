#!/usr/bin/env python

def digit_set(n):
  n_set = set()
  while n > 0:
    n_set.add(n%10)
    n /= 10
  return n_set

n = 125874
multiples = [1,2,3,4,5,6]
while(True):
  n += 1
  #if n % 1000 == 0:
  #  print "trying {}".format(n)
  n_set = digit_set(n)
  for m in multiples:
    if n_set != digit_set(m*n):
      # not the same digits, stop searching
      break
  else: # all the multiples were the same
    print n
    #for m in multiples:
    #  print "{} * {} = {}".format(n,m,n*m)
    break # while loop
