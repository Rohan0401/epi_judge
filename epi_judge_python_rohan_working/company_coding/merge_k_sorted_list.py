from __future__ import print_function
from heapq import *


class ListNode:
  def __init__(self, value):
    self.value = value
    self.next = None

  def __lt__(self, other):
      return self.value < other.value


def merge_lists(lists):
  #resultHead = None
  # TODO: Write your code here
  minHeap = []
  resultHead, resultTail = None, None
  # take all the root and add it to the heap
  for root in lists:
      if root != None:
          heappush(minHeap, root)
 # take the top element if it has next value put back to the heap
  while minHeap:
     node = heappop(minHeap)
     if resultHead == None:
         resultHead = resultTail = node
     else:
         resultTail.next = node
         resultTail = resultTail.next

     if node.next != None:
         heappush(minHeap, node.next)




  return resultHead


def main():
  l1 = ListNode(2)
  l1.next = ListNode(6)
  l1.next.next = ListNode(8)

  l2 = ListNode(3)
  l2.next = ListNode(6)
  l2.next.next = ListNode(7)

  l3 = ListNode(1)
  l3.next = ListNode(3)
  l3.next.next = ListNode(4)

  result = merge_lists([l1, l2, l3])
  print("Here are the elements form the merged list: ", end='')
  while result != None:
    print(str(result.value) + " ", end='')
    result = result.next


main()

