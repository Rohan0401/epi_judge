from collections import deque
def is_scheduling_possible(tasks, prerequisites):
  # TODO: Write your code here

  # Vertices are the task and Edges are the dependancy of the tasks
  if tasks <= 0:
      return False
  # First we have to create inDegree and graph for the program
  sortedOrder = []
  inDegree = {i : 0 for i in range(tasks)}
  graph = {parent : [] for parent in range(tasks)}

  # Build the graph for the problem with the inDegree of the edges

  for edge in prerequisites:
      parent, child = edge[0], edge[1]
      graph[parent].append(child)
      inDegree[child] += 1

  # Find all the children with 0 inDegree

  source = deque()


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


  if len(sortedOrder) != tasks:
      return False





  return True


def main():
  print("Is scheduling possible: " +
        str(is_scheduling_possible(3, [[0, 1], [1, 2]])))
  print("Is scheduling possible: " +
        str(is_scheduling_possible(3, [[0, 1], [1, 2], [2, 0]])))
  print("Is scheduling possible: " +
        str(is_scheduling_possible(6, [[0, 4], [1, 4], [3, 2], [1, 3]])))

main()
