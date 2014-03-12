#!/usr/bin/env python

from euler007 import eratosthenes
import time

def collatz_sequence(n):
    sequence = [n]
    while n > 1:
        n = (n/2) if n % 2 == 0 else (3*n+1)
        sequence.append(n)
    return sequence

def collatz_steps(n, memos):
    steps = 1
    while n > 1:
        n = (n/2) if n % 2 == 0 else (3*n+1)
        if n in memos:
            steps += memos[n]
            break
        else:
            steps += 1
    return steps


if __name__=="__main__":
    debugging = False
    tic = time.time()
    #primes = [2*e for e in eratosthenes(5*10**5)]
    numbers = [i for i in xrange(10*10**5, 5*10**5, -1)]

    # go backwards through the numbers
    steps = {}
    maxsteps = 0
    maxn = None
    for n in xrange(-1, -1-len(numbers), -1):
        steps[numbers[n]] = collatz_steps(numbers[n], steps)
        if steps[numbers[n]] > maxsteps:
            maxsteps = steps[numbers[n]]
            maxn = numbers[n]
        #print "{}: {} --> {} steps".format(-1*n, numbers[n], steps[numbers[n]])
    if debugging:
        print "max steps: {} --> {}".format(maxn, steps[maxn])
        print "{:0} s".format(int(time.time() - tic))
    else:
        print maxn
