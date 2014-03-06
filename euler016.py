#!/usr/bin/env python

'''
I was in the middle of implementing string-based binary long division,
then just tried it in the console.  Feels like cheating, but the problem is
easy with the right tools, I guess.
'''

print sum(int(s) for s in "{}".format(2**1000))
