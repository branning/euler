#!/usr/bin/env python

fname = "words.txt"
words = {}
max_value = 0
with open(fname, 'r') as f:
  for w in f.read().split(','):
    word = w.strip('"')
    words[word] = sum([ord(s)-ord('A')+1 for s in word])
    if words[word] > max_value:
      max_value = words[word]

triangle = set([0.5*n*(n+1) for n in range(max_value+1)][1:])

triangle_names = []
for w in words:
  if words[w] in triangle:
    triangle_names.append(w)
print len(triangle_names)
