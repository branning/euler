#!/usr/bin/env python

import math

def isPalindrome(x):
    return str(x) == str(analytical_reverse(x)).zfill(len(str(x)))

def analytical_reverse(n):
    power = int(math.floor(math.log10(n)))
    reversed = 0
    for p in range(power, -1, -1):
        reversed += n / 10**p * 10**(power-p)
        n -= n / 10**p * 10**p
    return reversed

def gridSearch(x_end, y_end):
    largest_palindrome = None
    found = False
    for x in xrange(999, x_end - 1, -1):
        for y in xrange(999, y_end - 1, -1):
            if isPalindrome(x*y):
                found = True
#               print "{} * {} is a palindrome!".format(x, y)
                largest_palindrome = x*y
                return largest_palindrome
                break
        if found:
            break

if __name__=="__main__":
    # It's likely the highest palindromic product is near 999 * 999. Look there
    print gridSearch(900,900)