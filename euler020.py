#!/usr/bin/env python

from math import factorial

n = factorial(100)
print sum([int(i) for i in "{}".format(n)])
