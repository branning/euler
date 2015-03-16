#!/usr/bin/env python

class Spiral(object):
  def __init__(self,N):
    if N % 2 != 1:
      print "N must be odd!"
      return
    values = [[None] * N for row in range(N)]
    coord = lambda x: x+N/2

    X = 0
    Y = 0
    n = 1
    values[coord(Y)][coord(X)] = n

    for rotation in range(1, N/2+1):
      n += 1
      X += 1 # move right 1
      values[coord(Y)][coord(X)] = n
      for down in range(rotation*2-1):
        n += 1
        Y += 1
        values[coord(Y)][coord(X)] = n
      for left in range(rotation*2):
        n += 1
        X -= 1
        values[coord(Y)][coord(X)] = n
      for up in range(rotation*2):
        n += 1
        Y -= 1
        values[coord(Y)][coord(X)] = n
      for right in range(rotation*2):
        n += 1
        X += 1
        values[coord(Y)][coord(X)] = n
    self.values = values

  def __repr__(self):
    repr = ''
    for line in self.values:
      repr += (" ".join(["{:3}".format(item) for item in line]) + '\n')
    repr.strip('\n')
    return repr

  def diagonals(self):
    diag1 = []
    diag2 = []
    for x in range(len(self.values)):
      diag1.append(self.values[x][x])
      diag2.append(self.values[len(self.values)-1-x][x])
    return diag1,diag2

debugging = False

spiral1001 = Spiral(1001)
if debugging:
  print spiral1001
diagonals = spiral1001.diagonals()
print sum(diagonals[0]) + sum(diagonals[1]) - 1
