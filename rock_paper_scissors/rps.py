#!/usr/bin/python

import sys




def rock_paper_scissors(n):
  options = ['rock', 'paper', 'scissors']
  allPoss = []
  if n == 0:
    return [[]]
  def roundChoice(round, roundNumber):
    
      for i in range(len(options)):
          round.append(options[i])
          if roundNumber == n :
            allPoss.append(list(round))
          else:
            roundChoice(round, roundNumber + 1)
          round.pop()
  roundChoice([], 1 )
  return allPoss
 
rock_paper_scissors(4)


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')