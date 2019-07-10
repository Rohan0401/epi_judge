"""
There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. Each task can have some prerequisite tasks which need to be completed before it can be scheduled. Given the number of tasks and a list of prerequisite pairs, write a method to print all possible ordering of tasks meeting all prerequisites.

Example 1:

Input: Tasks=3, Prerequisites=[0, 1], [1, 2]

Output: [0, 1, 2]

Explanation: There is only possible ordering of the tasks.

Example 2:

Input: Tasks=4, Prerequisites=[3, 2], [3, 0], [2, 0], [2, 1]

Output:

1) [3, 2, 0, 1]

2) [3, 2, 1, 0]

Explanation: There are two possible orderings of the tasks meeting all prerequisites.

Example 3:

Input: Tasks=6, Prerequisites=[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]

Output:

1) [0, 1, 4, 3, 2, 5]

2) [0, 1, 3, 4, 2, 5]

3) [0, 1, 3, 2, 4, 5]

4) [0, 1, 3, 2, 5, 4]

5) [1, 0, 3, 4, 2, 5]

6) [1, 0, 3, 2, 4, 5]

7) [1, 0, 3, 2, 5, 4]

8) [1, 0, 4, 3, 2, 5]

9) [1, 3, 0, 2, 4, 5]

10) [1, 3, 0, 2, 5, 4]

11) [1, 3, 0, 4, 2, 5]

12) [1, 3, 2, 0, 5, 4]

13) [1, 3, 2, 0, 4, 5]
"""
from collections import deque
def print_orders(tasks, prerequisites):
  # TODO: Write your code here


  # Intialize empty graph
  inDegree = {i:0 for i in range(tasks)}
  graph = {i: [] for i in range(tasks)}

  # Build the graph from the prerequisite
  for prereq in prerequisites:
      parent, child = prereq[0], prereq[1]
      graph[parent].append(child)
      inDegree[child] += 1

  # Create a source queue for processing graph
  sortedOrders = []
  sources = deque()
  for child in inDegree:
      if inDegree[child] == 0:
          sources.append(child)

          print_all_scheduled_tasks(graph, inDegree, sources, sortedOrders)



def print_all_scheduled_tasks(graph, inDegree, sources, sortedOrders):
     if sources:
         for vertex in sources:
             sortedOrders.append(vertex)

             sourcesForNextCall = deque(sources) # make a copy for next call

             # Remove the current sources and keep rest of them in queue

             sourcesForNextCall.remove(vertex)
             for child in graph[vertex]:
                 inDegree[child] -= 1
                 if inDegree[child] == 0:
                     sourcesForNextCall.append(child)

             print_all_scheduled_tasks(graph, inDegree, sourcesForNextCall, sortedOrders)

             sortedOrders.remove(vertex)
             for child in graph[vertex]:
                 inDegree[child] += 1

     if len(sortedOrders) == len(inDegree):
         print(sortedOrders)






def main():
  # print("Task Orders: ")
  # print_orders(3, [[0, 1], [1, 2]])

  print("Task Orders: ")
  print_orders(4, [[3, 2], [3, 0], [2, 0], [2, 1]])

  print("Task Orders: ")
  print_orders(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])


main()
