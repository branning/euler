#!/usr/bin/env python

two,three,four,five,six,seven,eight,nine,ten,jack,queen,king,ace = range(13)
highcard,onepair,twopair,threeofakind,straight,flush,fullhouse,fourofakind,straightflush,royalflush = range(10)
handname = ['highcard','onepair','twopair','threeofakind','straight','flush','fullhouse','fourofakind','straightflush','royalflush']

cards = {"2": two,
         "3": three,
         "4": four,
         "5": five,
         "6": six,
         "7": seven,
         "8": eight,
         "9": nine,
         "T": ten,
         "J": jack,
         "Q": queen,
         "K": king,
         "A": ace,
        }

def score(hand):
  suits = set([card[1] for card in hand])
  cards = [card[0] for card in hand]
  cards.sort()
  counts = {}
  for c in cards:
    if c not in counts:
      counts[c] = 1
    else:
      counts[c] += 1
  if len(suits)==1 and cards == range(jack,ace+1):
    return royalflush,[]
  elif len(suits)==1 and all([cards[i]+1==cards[i+1] for i in range(4)]):
    return straightflush,[max(cards)]
  elif max(counts.values()) == 4:
    return fourofakind,[c for c in counts if counts[c]==4]
  elif set(counts.values()) == set([2,3]):
    tiebreaker = []
    for c in counts:
      if counts[c]==3:
        tiebreaker.append(c)
        break
    for c in counts:
      if counts[c]==2:
        tiebreaker.append(c)
        break
    return fullhouse,tiebreaker
  elif len(suits)==1:
    return flush,[max(cards)]
  elif all([cards[i]+1==cards[i+1] for i in range(4)]):
    return straight,[max(cards)]
  elif max(counts.values()) == 3:
    return threeofakind,[c for c in counts if counts[c]==3]
  elif sorted(counts.values())[1:] == [2,2]:
    return twopair,[c for c in counts if counts[c]==2]
  elif max(counts.values()) == 2:
    tiebreaker = [c for c in counts if counts[c]==2]
    tiebreaker.append(max(set(cards) - set(tiebreaker)))
    return onepair,tiebreaker
  else:
    return highcard,[max(cards)]

wins = [] # either A or B

with open('data/poker.txt', 'r') as input:
  for line in input:
    allcards = line.strip().split(' ')
    handA = [(cards[c[0]],c[1]) for c in allcards[:5]]
    scoreA,tiebreakerA = score(handA)
    handB = [(cards[c[0]],c[1]) for c in allcards[5:]]
    scoreB,tiebreakerB = score(handB)
    if scoreA > scoreB:
      wins.append('A')
    elif scoreB > scoreA:
      wins.append('B')
    else:
      for tieA,tieB in zip(tiebreakerA, tiebreakerB):
        if tieA > tieB:
          wins.append('A')
          break
        elif tieB > tieA:
          wins.append('B')
          break
      else:
        print "Tie! both have {}".format(handname[scoreA])
        print "hand A: {}".format(handA)
        print "hand B: {}".format(handB)
        wins.append('T')

print len(filter(lambda x: x=='A', wins))
