#!/usr/bin/env python

'''
Run all the solutions for which we know the ansewr, and check them.
'''

import subprocess

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
          15 : 137846528820
}

#import pdb; pdb.set_trace()

for problem in answer.keys():
    filename = 'euler' + str(problem).zfill(3) + '.py'
    print "{} ...".format(filename),
    result = subprocess.check_output(['python',filename])
    result = int(result.strip())
    if result != answer[problem]:
        print "failed! Expected {}, got {}".format(answer[problem], result)
    else:
        print u'\u221a'
