# Problem Statement
#
# Given a string and a number ‘K’, find if the string can be rearranged such that the same characters are at least ‘K’ distance apart from each other.
"""
Example 1:

Input: "Programming", K=3

Output: "rgmPrgmiano" or "gmringmrPoa"

Explanation: All same characters are 3 distance apart.

Example 2:

Input: "aappa", K=3

Output: ""

Explanation: We cannot find an arrangement of the string where any two 'a' are 3 distance apart.

"""
from collections import deque
from heapq import *
def reorganize_string(str, k):
  # TODO: Write your code here
  charMap = {}
  for char in str:
      charMap[char] = charMap.get(char, 0) + 1
  maxHeap = []
  for word, frequency in charMap.items():
      heappush(maxHeap, (-frequency, word))
  result = []
  prevChar, prevFreq = None, 0
  # print(maxHeap)
  queue = deque()
  while maxHeap:
      frequency, word = heappop(maxHeap)
      result.append(word)
      queue.append((word, frequency + 1))
      if len(queue) == k:
          word, frequency = queue.popleft()
          if -frequency > 0:
              heappush(maxHeap, (frequency, word))









  return "".join(result) if len(result) == len(str) else ""

def main():
  print("Reorganized string: " + reorganize_string("Programming", 3))
  print("Reorganized string: " + reorganize_string("aapa", 3))


main()
