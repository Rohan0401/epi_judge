"""
Problem Statement

Given ‘M’ sorted arrays, find the K’th smallest number among all the arrays.

Example 1:

Input: L1=[2, 6, 8], L2=[3, 6, 7], L3=[1, 3, 4], K=5

Output: 4

Explanation: The 5th smallest number among all the arrays is 4, this can be verified from the merged

list of all the arrays: [1, 2, 3, 3, 4, 6, 6, 7, 8]

Example 2:

Input: L1=[5, 8, 9], L2=[1, 7], K=3

Output: 7

Explanation: The 3rd smallest number among all the arrays is 7.

Try it yourself

Try solving this question here:


"""
from heapq import *
def find_Kth_smallest(lists, k):
  number = -1
  # TODO: Write your code here
  minHeap = []
  for i in range(len(lists)):
      heappush(minHeap, (lists[i][0], 0, lists[i]))

  numberCount, number = 0, 0

  while minHeap:
      number, i , single_list = heappop(minHeap)
      numberCount += 1
      if numberCount == k:
          break
      if len(single_list) > i+1:
          heappush(minHeap, (single_list[i+1], i + 1, single_list))


  return number


def main():
  print("Kth smallest number is: " +
        str(find_Kth_smallest([[2, 6, 8], [3, 6, 7], [1, 3, 4]], 5)))


main()
