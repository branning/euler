#!/usr/bin/env python

coins = [1, 2, 5, 10, 20, 50, 100, 200]
combinations = {}

limit = 200 # 200p = 2 pound

c = 0 # 1p
for value in range(limit+1):
  combinations[value, c] = 1

for value in range(limit+1):
  for c in range(1,len(coins)):
    combinations[value,c] = 0
    if value >= coins[c]:
      combinations[value,c] += combinations[value,c-1]
      combinations[value,c] += combinations[value-coins[c], c]
    else:
      combinations[value,c] += combinations[value,c-1]

debugging = False
if debugging:
  for value in range(limit+1):
    print "{}: {}".format(value, ' '.join([str(combinations[value,c]) for c in range(len(coins))]))
else:
  print combinations[limit,len(coins)-1]
