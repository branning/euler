#!/usr/bin/env python

from euler007 import eratosthenes

def consecutive_prime_sum(limit):
  primes = eratosthenes(limit)
  primes_set = set(primes)

  # find maximum window size
  window = 0
  while sum(primes[:window]) < limit:
    window += 1
  window -= 1 # back off 1

  while window > 0:
    for p in range(len(primes) - window):
      window_sum = sum(primes[p:p+window])
      if window_sum in primes_set:
        #print "sum of {} primes is {} -- {}".format(window, window_sum, primes[p:window+p])
        return window, p, window_sum
      elif p > limit:
        window -= 1
        break # go to next window size
    else:
      window -= 1

#window, p, wsum = consecutive_prime_sum(100)
#window, p, wsum = consecutive_prime_sum(1000)
window, p, wsum = consecutive_prime_sum(10**6)
print wsum
