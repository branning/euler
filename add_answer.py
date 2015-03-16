#!/usr/bin/env python

import bcrypt
import cPickle
import sys

def pairs(stream):
    for i in xrange(0, len(stream), 2):
        yield stream[i:i+2]

if __name__=="__main__":
    with open('answers.p', 'rb') as answers_pickle:
        answers = cPickle.load(answers_pickle)
    new_answers = {}
    for problem, answer in pairs(sys.argv[1:]):
        print "{:4} {:12}".format(problem, answer)
        new_answers[problem] = bcrypt.hashpw(str(answer), bcrypt.gensalt())
    print "Add these answers?"
    if raw_input('Add these answers? (y/n)').lower() == 'y':
        updated_answers = answers.copy()
        updated_answers.update(new_answers)
    print updated_answers

