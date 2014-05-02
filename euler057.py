#!/usr/bin/env python

from euler003 import GCD
from math import log10, ceil

def reduce_fraction(num,den):
  divisor = GCD(num, den)
  num /= divisor
  den /= divisor
  return num, den

def continued_fraction(n):
  '''
  n is a list representation of a contiued fraction
  '''
  # if n[0] is 0, then it's less than 1.  find rational representation
  # of its reciprocal, then swap numerator and denominator
  if n[0] == 0:
    num,den = continued_fraction(n[1:])
    return den,num

  # proper makes a proper fractions of the form x + 1/(y[0]/y[1])
  proper = lambda y,x: (x*y[0] + y[1], y[0])
  # seed the last term with a denominator of 1
  #n[-1] = (n[-1],1)
  num, den = reduce(proper, reversed(n[:-1] + [[n[-1],1]] ))

  return num,den


if __name__=="__main__":
  num_greater = 0
  iterations = 1000
  a = [1]
  for i in range(iterations):
    a.append(2)
    num,den = continued_fraction(a)
    num, den = reduce_fraction(num,den)
    # See if there are more digits in numberator than denominator
    if ceil(log10(num)) > ceil(log10(den)):
      num_greater += 1
      #print '* ',num,den
  print num_greater
