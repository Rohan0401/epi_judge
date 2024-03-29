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
Another way of defining the rotation is to take the sub-list of ‘k’ ending nodes of the LinkedList and connect them to the beginning. Other than that we have to do three more things:

Connect the last node of the LinkedList to the head, because the list will have a different tail after the rotation.
The new head of the LinkedList will be the node at the beginning of the sublist.
The node right before the start of sub-list will be the new tail of the rotated LinkedList.


"""

def rotate(head, rotations):
  # TODO: Write your code here

  if head is None or rotations <= 0:
      return head

  last_node = head # connect last node to the head of the list
  list_length = 1 # find the list length

  while last_node.next is not None:
      last_node = last_node.next
      list_length += 1
  last_node.next = head
  rotations %= list_length # no need to roate more than list length

  skip_length = list_length - rotations

  last_node_of_rotated_list = head # make last node with the head the new tail is different

  for i in range(1, skip_length):
    last_node_of_rotated_list  = last_node_of_rotated_list.next

   # last node of rotated list is the head of new list

  head = last_node_of_rotated_list.next

  last_node_of_rotated_list.next = None

  return head




def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = rotate(head, 3)
  print("Nodes of rotated LinkedList are: ", end='')
  result.print_list()


main()
