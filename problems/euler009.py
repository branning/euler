from euler007 import eratosthenes


def stirling_count(n, k):
    # number of ways to partition set of size n into k blocks
    if n == 0 and k == 0:
        return 1
    elif n == 0 or k == 0:
        return 0
    return k * stirling_count(n-1,k) + stirling_count(n-1,k-1)

def hamming(base, target):
    # computer base-2 Hamming distance between base and target
    # base and target should be intergers
    binary_strings = ["{:b}".format(i) for i in (base, target)]
    binary_strings = [i.zfill(max([len(b) for b in binary_strings])) for i in binary_strings]
    return sum([b!=t for b,t in zip(binary_strings[0], binary_strings[1])])

def stirling2(a):
    import pdb; pdb.set_trace()
    # a is a set, k is the number of bins
    subsets = []
    max_hamming = len(a)/2
    for code_num in range(1, 2**len(a) - 1):
        if hamming(0, code_num) > max_hamming:
            continue
        code = "{:b}".format(code_num).zfill(len(a))
        left = set()
        right = set()
        for ai,c in zip(a, code):
            if c is '0':
                left.add(ai)
            else:
                right.add(ai)
        subsets.append((left,right))
    return subsets

def euclid_pythagorean_triplet(m, n):
    # m > n
    # m and n must be coprime
    # one of {m,n} must be even
    a = m**2 - n**2
    b = 2*m*n
    c = m**2 + n**2
    return (a,b,c)

def invert_triple(a,b,c):
    # find m, n, and k that generate a triplet
    pass


def euclid_pythagorean_triplet(limit=100):

    return "This is unfinished!"
    primes = eratosthenes(limit)

    # first generate primitive triples


    # add a prime, then compute co-prime set (m,n) by combining primes
    #for bin_a in range(1:len(primes)/2):

########## UNFINISHED





def findabc():
    return "This is unfinished!"
    inequality = lambda a,b,c: a < b and b < c
    pythagorus = lambda a,b,c: a*a + b*b - c*c == 0

########## UNFINISHED

# I did this by hand, eventually
# Using the Euclid formulas for generating a Pythagorean triple, and the constraint
# of the problem, a + b + c = 1000
# a = m**2 - n**2
# b = 2*m*n
# c = m**2 + n**2
# So, m**2 - n**2 + 2*m*n + m**2 + n**2 = 1000
# combine m**2, cancel n**2
# 2*m(m+n) = 1000
# m*(m+n) = 500
# Guess checked this.  Sqrt(500) = 22.+, needed to split this into a perfect square
# and a product of the square's factor and another number
# Tried m=20, m**2 = 400.  (500-400) / 20 = 5
# So, m=20, n=5
# a = 20**2 - 5**2 = 375
# b = 2*20*5 = 200
# c = 20**2 + 5**2 = 425
# 375 + 200 + 425 == 1000
print 375*200*425
