#!/usr/bin/env python

from euler004 import isPalindrome

debugging = False
if debugging:
	limit = 10**3
else:
	limit = 10**6

double_palindromes = []

for i in range(1,limit):
	if isPalindrome(i): # in base 10
		bin_i = "{:b}".format(i)		
		for j in range(len(bin_i)/2):
			if bin_i[j] != bin_i[len(bin_i)-1 - j]:
				break
		else:
			# passed all the comparisons, it's a palindrome
			if debugging:
				print "{} and {} are both palindromes".format(i, bin_i)
			double_palindromes.append((i,bin_i))

print sum([x for x,b in double_palindromes])
