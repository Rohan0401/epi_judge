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


def reverse_alternate_k_elements(head, k):
  # TODO: Write your code here
  if k <= 1 or head is None:
      return head
  current, previous = head, None
  # Start reversing

  while True:

      last_node_from_previous_node = previous # last node from the previous list

      last_node_from_sub_list = current # last node from the sublist
      next = None # temp store a variable

      # reverse

      i = 0
      while current is not None and i < k :
          next = current.next
          current.next = previous
          previous = current
          current = next

          i += 1

      # connect with the previous part
      if last_node_from_previous_node is not None:
         last_node_from_previous_node.next = previous
      else:
         head = previous

      # connect with the next part
      last_node_from_sub_list.next = current


      # skip rows
      i = 0
      while current is not None and i < k:
          previous = current
          current = current.next
          i += 1

     # if the list terminate
      if current is None:
          break

  return head


def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)
  head.next.next.next.next.next.next = Node(7)
  head.next.next.next.next.next.next.next = Node(8)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = reverse_alternate_k_elements(head, 2)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()


main()
