from __future__ import print_function


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(str(temp.value) + " ", end='')
      temp = temp.next
    print()


def reorder(head):
  # TODO: Write your code here
  if head is None or head.next is None:
      return head

  slow, fast = head, head

  while fast is not None and fast.next is not None:
      slow = slow.next
      fast = fast.next.next


  first_half = head
  second_half = reverse_list(slow)

  while first_half is not None and second_half is not None:

      out_list = first_half.next
      first_half.next = second_half
      first_half = out_list

      out_list = second_half.next
      second_half.next = first_half
      second_half = out_list

  if first_half is not None:
      first_half.next = None


def reverse_list(head):

    previous, current, next = None, head, None

    while current is not None:
        next = current.next
        current.next = previous
        previous = current
        current = next

    return previous

def main():
  head = Node(2)
  head.next = Node(4)
  head.next.next = Node(6)
  head.next.next.next = Node(8)
  head.next.next.next.next = Node(10)
  head.next.next.next.next.next = Node(12)
  reorder(head)
  head.print_list()


main()
