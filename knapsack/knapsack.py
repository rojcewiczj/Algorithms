#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])
file_contents = open('c:/Users/rojce/documents/GitHub/Algorithms/knapsack/data/small3.txt', 'r')
small_1_items = []
    
for line in file_contents.readlines():
    data = line.rstrip().split()
    small_1_items.append(Item(int(data[0]), int(data[1]), int(data[2])))

    file_contents.close()


def knapsack_solver(items, capacity):
  bag= []
  total_cost = 0
  value_index = 0
  total_value = 0 
  values=[]
  maybe_bag={}
  size_bag={}
  for item in items:
     maybe_bag[item.value/item.size] = [item.index, item.size, item.value]
     values.append(item.value/item.size)
  values = sorted(values, reverse = True)

  for value in values:
  
      if total_cost + maybe_bag[value][1] > capacity:
         break
      else:
        total_cost = total_cost + maybe_bag[value][1]
        total_value += maybe_bag[value][2]
        bag.append(int(maybe_bag[value][0]))
  print(total_value)
  print(sorted(bag))
  return{'Value': int(total_value), 'Chosen': sorted(bag)}
  
  # for value in values:
  #   print(maybe_bag[value][0])
    
  # for item in values:
  #   if capacity == 0:
  #      bag.append({'Value': totalValue , 'Chosen': chosenIndex})
  #      return bag
    
 

print(knapsack_solver(small_1_items, 100))
if __name__ == '__main__':
  if len(sys.argv) > 1:
    capacity = int(sys.argv[2])
    file_location = sys.argv[1].strip()
    file_contents = open(file_location, 'r')
    items = []

    for line in file_contents.readlines():
      data = line.rstrip().split()
      items.append(Item(int(data[0]), int(data[1]), int(data[2])))
    
    file_contents.close()
    print(knapsack_solver(items, capacity))
  else:
    print('Usage: knapsack.py [filename] [capacity]')