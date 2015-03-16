#!/usr/bin/env python

def brutewalk(t):
  # walk all the paths, return max sum path
  max = 0
  maxpath = None
  for i in range(2**( len(t)-1 )):
    pos = 0
    path = [t[0][0]]
    for i,b in enumerate("{:b}".format(i)):
      if b=='0':
        path.append(t[i+1][pos])
      else:
        pos = pos + 1
        path.append(t[i+1][pos])
    if sum(path) > max:
      max = sum(path)
      maxpath = path
  return maxpath

def astar(t):
  # return path with highest value
  # cost is defined sum of numbers we can't reach due to the chosen path
    path = [(0, t[0][0])]
    pos = 0
    cost = 0
    for line in range(1,len(t)):
      rightsum = sum([t[i][i] for i in range(line,len(t))])
      leftsum = sum([t[i][pos] for i in range(line,len(t))])
      if rightsum > leftsum:
        cost = leftsum
        pos = pos + 1
        path.append((cost, t[line][pos]))
      else:
        cost = rightsum
        path.append((cost, t[line][pos]))
    return path


if __name__=="__main__":
  triangle_str = ("75",
  "95 64",
  "17 47 82",
  "18 35 87 10",
  "20 04 82 47 65",
  "19 01 23 75 03 34",
  "88 02 77 73 07 63 67",
  "99 65 04 28 06 16 70 92",
  "41 41 26 56 83 40 80 70 33",
  "41 48 72 33 47 32 37 16 94 29",
  "53 71 44 65 25 43 91 52 97 51 14",
  "70 11 33 28 77 73 17 78 39 68 17 57",
  "91 71 52 38 17 14 91 43 58 50 27 29 48",
  "63 66 04 68 89 53 67 30 73 16 69 87 40 31",
  "04 62 98 27 23 09 70 98 73 93 38 53 60 04 23")

  triangle = []
  for line in triangle_str:
      triangle.append([int(i) for i in line.split(' ')])

  maxpath = brutewalk(triangle)
  print sum(maxpath)
