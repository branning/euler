#!/usr/bin/env python

from euler007 import eratosthenes

'''
http://mathworld.wolfram.com/RepeatingDecimal.html
http://mathworld.wolfram.com/MultiplicativeOrder.html
'''

def MultiplicativeOrder10(n):
  '''
  returns multiplicative order of 10 mod n
  this is equal to the length of the period of the decimal
  expansion of 1/n
  '''
  limit = 1000
  for i in range(2,limit):
    if 10**i % n == 1:
      return i
  else:
    return None

def DecimalExpansionPrimes(debugging=True):
  limit = 1000
  primes = eratosthenes(limit)

  decimal_period = {2: 0,
                    3: 1,
                    5: 0}
  for p in primes[3:]:
    mult_order = MultiplicativeOrder10(p)
    decimal_period[p] = mult_order
  max_n = 0
  max_length = 0
  for n in decimal_period:
    if decimal_period[n] > max_length:
      max_n = n
      max_length = decimal_period[n]
  if debugging:
    print "max period is {} for 1/{}".format(max_length, max_n)
  else:
    print max_n

if __name__=="__main__":
  DecimalExpansionPrimes(False)
