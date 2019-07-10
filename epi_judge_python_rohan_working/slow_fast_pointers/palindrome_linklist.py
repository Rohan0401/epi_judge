class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next


def is_palindromic_linked_list(head):
  # TODO: Write your code here

  if head is None or head.next is None:
      return True

  slow, fast = head, head

  while fast is not None and fast.next is not None:
      slow = slow.next
      fast = fast.next.next

  head_second_half = reverse_list(slow) # reverse second half

  # store a copy to revert back
  copy_of_second_half = head_second_half

  while head is not None and head_second_half is not None:
      if head.value != head_second_half.value: # compare or iterate
          break
      head = head.next
      head_second_half = head_second_half.next


  reverse_list(copy_of_second_half)

  if head is None or head_second_half is None:
      return True

  return False

def reverse_list(head, previous=None):
    if head is None or head.next is None:
        return head
    previous, current, next = previous, head, None

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
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(2)

  print("Is palindrome: " + str(is_palindromic_linked_list(head)))

  head.next.next.next.next.next = Node(2)
  print("Is palindrome: " + str(is_palindromic_linked_list(head)))


main()







