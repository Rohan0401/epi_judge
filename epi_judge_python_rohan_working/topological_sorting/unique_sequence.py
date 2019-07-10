from collections import deque
def can_construct(originalSeq, sequences):
  # TODO: Write your code here
  if len(originalSeq) <= 0:
    return False
  sortedOrder = []
  # Init a graph and a inDegree
  graph = {}
  inDegree = {}
  for seq in sequences:
    for num in seq:
      graph[num] = []
      inDegree[num] = 0

  # Build The graph
  for seq in sequences:
    for i in range(1, len(seq)):
      parent, child = seq[i-1], seq[i]
      graph[parent].append(child)
      inDegree[child] += 1


  # check the sequence length
  if len(originalSeq) != len(inDegree):
    return False




  # Get all the Sources with 0 inDegree
  source = deque()
  for key in inDegree:
    if inDegree[key] == 0:
      source.append(key)

  # start poping vertex from the source

  while source:

    if len(source) > 1: # more than one source
      return False

    if originalSeq[len(sortedOrder)] != source[0]: # next source is different in original sequence
      return False

    vertex = source.popleft()
    sortedOrder.append(vertex)

    for child in graph[vertex]:
      inDegree[child] -= 1
      if inDegree[child] == 0:
        source.append(child)


  return len(sortedOrder) == len(originalSeq)









def main():
  print("Can construct: " +
        str(can_construct([1, 2, 3, 4], [[1, 2], [2, 3], [3, 4]])))
  print("Can construct: " +
        str(can_construct([1, 2, 3, 4], [[1, 2], [2, 3], [2, 4]])))
  print("Can construct: " +
        str(can_construct([3, 1, 4, 2, 5], [[3, 1, 5], [1, 4, 2, 5]])))


main()
