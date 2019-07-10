"""
Problem Statement

You are given a list of tasks that need to be run, in any order, on a server.
Each task will take one CPU interval to execute but once a task has finished,
it has a cooling period during which it can’t be run again.
If the cooling period for all tasks is ‘K’ intervals,
find the minimum number of CPU intervals that the server needs to finish all tasks.

If at any time the server can’t execute any task then it must stay idle.

Example 1:

Input: [a, a, a, b, c, c], K=2

Output: 7

Explanation: a -> c -> b -> a -> c -> idle -> a

Example 2:

Input: [a, b, a], K=3

Output: 5

Explanation: a -> b -> idle -> idle -> a

Try it yourself

Try solving this question here:


"""

from heapq import *
from collections import deque
def schedule_tasks(tasks, k):
  intervalCount = 0
  taskMap = {}
  maxheap = []
  for task in tasks:
      taskMap[task] = taskMap.get(task, 0) + 1
  for task, frequency in taskMap.items():
      heappush(maxheap, (-frequency, task))



  while maxheap:
      waitList = []
      n = k + 1
      while n > 0 and maxheap:
          frequency, task = heappop(maxheap)
          intervalCount += 1
          if -frequency > 1:
              waitList.append((task, frequency+1))
          n -= 1

      for task, frequency in waitList:
          heappush(maxheap, (frequency, task))

      if maxheap:
          intervalCount += n


  # TODO: Write your code here
  return intervalCount


def main():
  print("Minimum intervals needed to execute all tasks: " +
        str(schedule_tasks(['a', 'a', 'a', 'b', 'c', 'c'], 2)))
  print("Minimum intervals needed to execute all tasks: " +
        str(schedule_tasks(['a', 'b', 'a'], 3)))


main()

