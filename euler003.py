#!/usr/bin/env python

# Euclid's GCD algorithm
def GCD(a, b):
    #if b == 0 and a != 0:
    #    return a
    #return GCD(b, a % b)
    while True:
      if b == 0 and a != 0:
          return a
      a,b = b, a % b

# Pollard's rho algorithm
def rho(a):
    f = lambda x : (x**2 - 1) % a
    x = 2
    y = 2
    d = 1
    while d==1:
        x = f(x)
        y = f(f(y))
        d = GCD(abs(x-y), a)
    if d == a:
        return None
    else:
        return d

def run(number):
    primes = []
    factors = []
    a = number
    while True:
        factor = rho(a)
        if factor is None:
#            print "rho failed for {}".format(a)
            primes.append(a)
            break
        else:
            factors.append(factor)
            a = a / factor

    # I was sort of finding the answer by trial and error here
    # The variable names are bad.  I hypothesized that the prime factors
    # would be the correct answer.  Looks like that's true?
#    print "Prime? factors of {}: {}".format(number, primes)
#    print "Factors of {}: {}".format(number, factors)
    print primes[0]

if __name__=="__main__":
    number = 600851475143
    run(number)
