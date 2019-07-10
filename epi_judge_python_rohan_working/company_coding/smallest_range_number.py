from heapq import *
import math
def find_smallest_range(lists):
  # TODO: Write your code here
  minHeap = []
  rangeSmaall, rangeLarge = 0 , math.inf
  currentMax  = -math.inf
  # Take the first element from the arr and push it to heap
  for elist in lists:
      currentMax = max(currentMax, elist[0])
      heappush(minHeap, (elist[0], 0, elist))

  # take the smallest element from the heap and if it gives us smaller range, update the ranges
  while len(minHeap) == len(lists):
      num, i, single_list = heappop(minHeap)
      if rangeLarge - rangeSmaall > currentMax - num:
          rangeSmaall = num
          rangeLarge = currentMax
      if len(single_list) > i+1:
          heappush(minHeap, (single_list[i+1], i+1, single_list))
          currentMax = max(currentMax, single_list[i+1])





  return [rangeSmaall, rangeLarge]


def main():
  print("Smallest range is: " +
        str(find_smallest_range([[1, 5, 8], [4, 12], [7, 8, 10]])))


main()

