"""
Problem Statement

There is a dictionary containing words from an alien language for which we don’t know the ordering of the characters.
Write a method to find the correct order of characters in the alien language.

Example 1:

Input: Words: ["ba", "bc", "ac", "cab"]

Output: bac

Explanation: Given that the words are sorted lexicographically by the rules of the alien language, so

from the given words we can conclude the following ordering among its characters:

​

1. From "ba" and "bc", we can conclude that 'a' comes before 'c'.

2. From "bc" and "ac", we can conclude that 'b' comes before 'a'

​

From the above two points we can conclude that the correct character order is: "bac"

Example 2:

Input: Words: ["cab", "aaa", "aab"]

Output: cab

Explanation: From the given words we can conclude the following ordering among its characters:

​

1. From "cab" and "aaa", we can conclude that 'c' comes before 'a'.

2. From "aaa" and "aab", we can conclude that 'a' comes before 'b'

​

From the above two points, we can conclude that the correct character order is: "cab"

Example 3:

Input: Words: ["ywx", "xww", "xz", "zyy", "zwz"]

Output: yxwz

Explanation: From the given words we can conclude the following ordering among its characters:

​

1. From "ywx" and "xww", we can conclude that 'y' comes before 'x'.

2. From "xww" and "xz", we can conclude that 'w' comes before 'z'

3. From "xz" and "zyy", we can conclude that 'x' comes before 'z'

2. From "zyy" and "zwz", we can conclude that 'y' comes before 'w'

​

From the above two points we can conclude that the correct character order is: "yxwz"

"""
from collections import deque

def find_order(words):
  # TODO: Write your code here

  # Build a graph intial
  inDegree = {}
  graph = {}

  for word in words:
      for char in word:
          graph[char] = []
          inDegree[char] = 0

  for i in range(0, len(words) - 1):
       w1 , w2 = words[i], words[i+1]
       for j in range(min(len(w1), len(w2))):
           parent, child = w1[j], w2[j]
           if parent != child:
               graph[parent].append(child)
               inDegree[child] += 1
               break

  #
  # for edge in edges:
  #     parent, child = edge[0], edge[1]
  #     if parent != child:
  #         graph[parent].append(child)
  #         inDegree[child] += 1

  source = deque()
  sortedOrder = []
  for key in inDegree:
      if inDegree[key] == 0:
          source.append(key)

  while source:
      vertex = source.popleft()
      sortedOrder.append(vertex)
      for child in graph[vertex]:
          inDegree[child] -= 1
          if inDegree[child] == 0:
              source.append(child)

  if len(sortedOrder) != len(graph):
       return ""

  return "".join(sortedOrder)




def main():
  print("Character order: " + find_order(["ba", "bc", "ac", "cab"]))
  print("Character order: " + find_order(["cab", "aaa", "aab"]))
  print("Character order: " + find_order(["ywx", "xww", "xz", "zyy", "zwz"]))
  print("Character order: " + find_order(["ywx", "xwy"]))


main()
