#!/usr/bin/env python

# Python doesn't have the integer limit issue this problem was designed
# to test
print sum(range(1,101))**2 - sum([i*i for i in range(1,101)])
