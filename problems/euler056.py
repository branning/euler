#!/usr/bin/env python

maxsum = 0
for p in range(1,100):
 for n in range(1,100):
   i = n**p
   digit_sum = 0
   while(i > 0):
       digit_sum += i % 10
       i /= 10
   if digit_sum > maxsum:
       maxsum = digit_sum
       max_n,max_p = n,p
print maxsum
