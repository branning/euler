#!/usr/bin/env python

def fibonacci(n):
  a = 1
  b = 1
  c = None
  for i in xrange(2,n):
    c = a + b
    a = b
    b = c
    yield(c)

if __name__=="__main__":
  for i,fib in enumerate(fibonacci(10000)):
    if len(str(fib)) >= 1000:
      print i+3
      break
