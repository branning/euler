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
    remove_answers = []
    for problem, answer in pairs(sys.argv[1:]):
        problem = int(problem)
        if answer == "remove":
            remove_answers.append(problem)
            print "{:4} remove".format(problem)
            continue
        print "{:4} {}".format(problem, answer),
        print "*changed" if problem in answers else ''
        new_answers[problem] = bcrypt.hashpw(str(answer), bcrypt.gensalt())
    if raw_input('Add these answers? (y/n)').lower() == 'y':
        answers.update(new_answers)
        for answer in remove_answers:
            del(answers[answer])
    with open('answers.p', 'w') as answers_pickle:
        cPickle.dump(answers, answers_pickle)
        print "{} answers written to {}".format(len(answers), answers_pickle.name)

