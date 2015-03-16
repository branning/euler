#!/usr/bin/env python

# this barely works, but does output correct words up to 1000
def num2words(n):
    onesteens = { 1 : "one",
                2 : "two",
                3 : "three",
                4 : "four",
                5 : "five",
                6 : "six",
                7 : "seven",
                8 : "eight",
                9 : "nine",
               10 : "ten",
               11 : "eleven",
               12 : "twelve",
               13 : "thirteen",
               14 : "fourteen",
               15 : "fifteen",
               16 : "sixteen",
               17 : "seventeen",
               18 : "eighteen",
               19 : "nineteen"
    }
    tens = { 2 : "twenty",
            3 : "thirty",
            4 : "forty",
            5 : "fifty",
            6 : "sixty",
            7 : "seventy",
            8 : "eighty",
            9 : "ninety",
    }
    powersoften = { 100 : "hundred",
                  1000 : "thousand"
    }

    words = []
    if n > 999:
        thousands = n / 1000
        words.extend([onesteens[thousands], "thousand"])
    if n % 1000 > 99:
        hundreds = n / 100
        words.extend([onesteens[hundreds], "hundred"])
    if n % 100 != 0 and n > 100:
        words.append("and")
    if n % 100 >= 20:
        words.append(tens[n % 100 / 10])
        if n % 10 != 0:
            words.append(onesteens[n % 10])
    elif n % 100 != 0 :
        words.append(onesteens[n % 100])
    return words

if __name__=="__main__":
    debugging = False
    sum = 0
    for i in range(1,1001):
        words = num2words(i)
        if debugging:
            print ' '.join(words)
        sum += len(''.join(words))
    print sum


