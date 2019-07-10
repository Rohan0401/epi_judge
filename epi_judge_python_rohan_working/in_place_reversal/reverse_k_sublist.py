from __future__ import print_function


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.value, end=" ")
      temp = temp.next
    print()
"""

    - Skip the first p-1 nodes, to reach the node at position p.
    - Remember the node at position p-1 to be used later to connect with the reversed sub-list.
    - Next, reverse the nodes from p to q using the same approach discussed in Reverse a LinkedList.
    - Connect the p-1 and q+1 nodes to the reversed sub-list.

"""

"""
1->2->3->4->5->6
   ^  ^


"""

def reverse_sub_list(head, p, q):
  # TODO: Write your code here
  # if head is None or head.next is None:
  #     return head
  if p == q:
      return head
  i = 0
  previous, current = None, head

  while current is not None and i < p-1:
      previous = current
      current = current.next
      i += 1

  last_node_at_p = previous
  last_node_at_q = current
  next = None


  i = 0
  while current is not None and i < q - p +1:
      next = current.next
      current.next = previous
      previous = current
      current = next
      i += 1

  if last_node_at_p is not None:
      last_node_at_p.next = previous
  else:
      head = previous

  last_node_at_q.next = current

  return head


def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = reverse_sub_list(head, 2, 4)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()


main()
