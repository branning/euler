#!/usr/bin/env python

def nextperm(s):
  '''
  http://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order
  '''
  k = None
  for i in range(len(s)-1):
    if s[i] < s[i+1]:
      k = i
  if k is None:
    # sequence in descending order, last permutation
    return None
  l = None
  for i in range(k+1, len(s)):
    if s[i] > s[k]:
      l = i
  hold = s[l]
  s[l] = s[k]
  s[k] = hold
  # reverse s from k+1 to the end
  t = s[k+1:]
  t.reverse()
  s[k+1:] = t
  return s

if __name__=="__main__":
  debugging = False
  s = range(10)
  permutations = 10**6-1
  for perm in xrange(permutations):
    nextperm(s)
    if debugging:
      print s
  print ''.join([str(n) for n in s])
