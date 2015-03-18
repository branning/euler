#!/usr/bin/env python

'''
Run all the solutions for which we know the ansewr, and check them.
'''

import bcrypt
import cPickle
import os.path
import subprocess
import sys
import time

with open('answers.p', 'rb') as answers_pickle:
    answers = cPickle.load(answers_pickle)

if __name__=="__main__":
    # problems as arguments to run selectively
    if len(sys.argv) > 1:
      problems = [int(a) for a in sys.argv[1:]]
    else:
      problems = answers.iterkeys()

    teststart = time.time()
    for problem in problems:
        if problem not in answers:
          print "Cannot test {}, we don't have an answer yet".format(problem)
          continue
        start = time.time()
        filename = 'euler' + str(problem).zfill(3) + '.py'
        filename = os.path.join("problems", filename)
        print "{} ...".format(filename),
        result = subprocess.check_output(['python',filename])
        result = result.strip()
        if bcrypt.hashpw(result, answers[problem]) != answers[problem]:
            print "failed! Proposed answer {} doesn't match hashed answer".format(answers[problem], result),
        else:
            print u'\u221a'.encode('utf-8'), # radical checkmark
        print "{0:.2f} s".format(time.time() - start)
    print "{0:.0f} s total".format(time.time() - teststart)

