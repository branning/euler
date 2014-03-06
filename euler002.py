#!/usr/bin/env python

import time

if __name__=="__main__":
    print "euler002"
    start = time.time()
    count = 0
    a, b = 1, 2
    sum = b # 1 is not even
    while True:
        c = a + b
        if c > 4000000:
            break
#        if c < 100000:
#            print c, " "
        count += 1
        if c % 2 == 0:
            sum += c
        a, b = b, c
    print sum, time.time() - start
