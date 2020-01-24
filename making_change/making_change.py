#!/usr/bin/python

import sys

def making_change(amount, denominations):
  my_array = [0]*(amount+1)
  if amount == 0:
    return 1
  else:
    for coin in denominations:
        for i in range(amount+1):
            if coin == i:
                my_array[i]+=1
            if i-coin>0:
                my_array[i]=((my_array)[i]+my_array[i-coin])
  return(my_array[-1])

print(making_change(0, [1, 5, 10, 25, 50]))


if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")