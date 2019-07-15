# Python program to print topological sorting of a DAG
from collections import defaultdict


# Class to represent a graph
class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # dictionary containing adjacency List
        self.V = vertices  # No. of vertices

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # recursive function

    def toposort_recur(self, node, visited, stack):

        # mark the visited
        visited[node] = True

        # recurse all childern
        for child in self.graph[node]:
            if not visited[child]:
                self.toposort_recur(child, visited, stack)

        stack.append(node)

    def topologicalSort(self):
        # Mark all the vertices as not visited
        visited = [False] * self.V
        stack = []
        for node in range(self.V):
            if not visited[node]:
                self.toposort_recur(node, visited, stack)

        print(stack[::-1])


g = Graph(6)
g.addEdge(5, 2);
g.addEdge(5, 0);
g.addEdge(4, 0);
g.addEdge(4, 1);
g.addEdge(2, 3);
g.addEdge(3, 1);

print("Following is a Topological Sort of the given graph")
g.topologicalSort()
# This code is contributed by Neelam Yadav
