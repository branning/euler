#!/usr/bin/env python

from operator import mul

from euler005 import factorize
from euler007 import eratosthenes

def triangle_numbers(limit):
    sum = 0
    for i in range(1,limit+1):
        sum += i
        yield sum

def prime_factorize(n, primes=None):
    if primes is None:
        primes = eratosthenes(n)
    factors = factorize(n, primes)
    prime_factors = {}
    for f in factors:
        if not prime_factors.has_key(f):
            prime_factors[f] = 1
        else:
            prime_factors[f] += 1
    return prime_factors

def divisors(n, primes=None):
    '''
    factors = prime_factorize(220)
    divisors = [2**(i%3)*5**((i/3)%2)*11**((i/6)%2) for i in range(12)]
    '''
    if primes is not None:
      factors = prime_factorize(n)
    else:
      factors = prime_factorize(n, primes)
    if n in primes:
      return [1, n]
    divisors = []
    try:
      num_divisors = reduce(mul, [factors[f]+1 for f in factors])
    except TypeError, e:
      import pdb; pdb.set_trace()
      print e
    for i in range(num_divisors):
      divisor = 1
      for fi,f in enumerate(factors):
        if fi > 0:
          inner_wheel = reduce(mul, map(lambda x:x+1, factors.values())[:fi])
        else:
          inner_wheel = 1
        divisor *= f**((i/inner_wheel)%(factors[f]+1))
        #print "{}**(({})%{})".format(f, i/inner_wheel, factors[f])
      divisors.append(divisor)
    divisors.sort()
    return divisors

def proper_divisors(n, primes):
  return divisors(n, primes)[:-1]

if __name__=="__main__":
    '''
    TODO: can improve performance?
    '''
    debugging = False

    limit = 100000
    primes = eratosthenes(limit)
    for i,t in enumerate(triangle_numbers(limit)):
        factors = prime_factorize(t, primes)
        divisors = 1 # include 1 for the number 1
        for f in factors.keys():
            divisors *= factors[f] + 1
        '''
        divisors = len(divisors(t, primes))
        '''
        if divisors > 500:
            if debugging:
                print "Triangle number {} is {} and has factors {} and therefore {} divisors".format(i, t, factors, divisors)
            else:
                print t
            break
