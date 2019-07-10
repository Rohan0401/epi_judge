from collections import deque
def find_trees(nodes, edges):
  # TODO: Write your code here

  # Init graph

  inDegree = {i: 0 for i in range(nodes)}
  graph = {i : [] for i in range(nodes)}

  # Build graph
  for edge in edges:
      n1, n2 = edge[0], edge[1]
      graph[n1].append(n2)
      graph[n2].append(n1)

      # Increment the degree
      inDegree[n1] += 1
      inDegree[n2] += 1

  # find the leaves with more than one inDegrees and append it to leaves

  leaves = deque()
  for node in inDegree:
      if inDegree[node] == 1:
          leaves.append(node)


  totalNodes = nodes

  while totalNodes > 2:
      leavesSize = len(leaves)
      totalNodes -= leavesSize
      for i in range(0, leavesSize):
          vertex = leaves.popleft()
          for child in graph[vertex]:
              inDegree[child] -= 1
              if inDegree[child] == 1:
                  leaves.append(child)

  return list(leaves)



  return []


def main():
  print("Roots of MHTs: " +
        str(find_trees(5, [[0, 1], [1, 2], [1, 3], [2, 4]])))
  print("Roots of MHTs: " +
        str(find_trees(4, [[0, 1], [0, 2], [2, 3]])))
  print("Roots of MHTs: " +
        str(find_trees(4, [[1, 2], [1, 3]])))


main()
