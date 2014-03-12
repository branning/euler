#!/usr/bin/env python

def factorial(n):
    f = 1
    for i in range(1,n+1):
        f *= i
    return f

# paths through (n,n) grid is equivalent to (n+n) choose n
# so, 40 choose 20,  40! / (20!20!)
print factorial(40) / (factorial(20)*factorial(20))
