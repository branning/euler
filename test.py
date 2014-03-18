#!/usr/bin/env python

'''
Run all the solutions for which we know the ansewr, and check them.
'''

import subprocess
import time

answer = { 1 : 233168,
           2 : 4613732,
           3 : 6857,
           4 : 906609,
           5 : 232792560,
           6 : 25164150,
           7 : 104743,
           8 : 40824,
          10 : 142913828922,
          11 : 70600674,
          12 : 76576500,
          13 : 5537376230,
          14 : 837799,
          15 : 137846528820,
          16 : 1366,
          17 : 21124,
          18 : 1074,
          19 : 171,
          20 : 648,
          21 : 31626,
          22 : 871198282,
          23 : 4179871,
          24 : 2783915460,
          25 : 4782,
          26 : 983,
          27 : -59231,
          28 : 669171001,
          29 : 9183
}

teststart = time.time()
for problem in answer.keys():
    start = time.time()
    filename = 'euler' + str(problem).zfill(3) + '.py'
    print "{} ...".format(filename),
    result = subprocess.check_output(['python',filename])
    result = int(result.strip()) # clean it up
    if result != answer[problem]:
        print "failed! Expected {}, got {}".format(answer[problem], result),
    else:
        print u'\u221a', # radical checkmark
    print "{0:.2f} s".format(time.time() - start)
print "{0:.0f} s total".format(time.time() - teststart)
