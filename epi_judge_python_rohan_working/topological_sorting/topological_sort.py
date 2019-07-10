from collections import deque
def topological_sort(vertices, edges):
  sortedOrder = []
  # TODO: Write your code here

  if vertices <= 0:
      return sortedOrder
  # A Intialization :
  # 1. Store the graph in a adjacency list which means vertex of all its children. Used dict where key is parent
  # and value is list contaning the children

  inDegree  = {i: 0 for i in range(vertices)}
  graph = {i: [] for i in range(vertices)}

  # 2. To find the souces we will keep the hashmap to count the in-degrees i.e. count the incoming edges of each vetex. Any vertex with
  # 0 in-degree will be the source
  #

  # build the graph

  for edge in edges:
      parent, child = edge[0], edge[1]
      graph[parent].append(child)
      inDegree[child] += 1

  # find all the sources with 0 inDegrees
  sources = deque()
  for key in inDegree:
      if inDegree[key] == 0:
          sources.append(key)

  # for each source add it to the sortedOrder and substract one from all its children degree
  # if a child in-degree becomes zero, add it tohe source queue

  while sources:
      vertex = sources.popleft()
      sortedOrder.append(vertex)
      for child in graph[vertex]:
          inDegree[child] -= 1
          if inDegree[child] == 0:
              sources.append(child)


  if len(sortedOrder) != vertices:
      return []




  return sortedOrder


def main():
  print("Topological sort: " +
        str(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]])))
  print("Topological sort: " +
        str(topological_sort(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]])))
  print("Topological sort: " +
        str(topological_sort(7, [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]])))


main()
