"""
Problem Statement

Design a class that simulates a Stack data structure, implementing the following two operations:

    push(int num): Pushes the number ‘num’ on the stack.
    pop(): Returns the most frequent number in the stack. If there is a tie, return the number which was pushed later.

Example:

After following push operations: push(1), push(2), push(3), push(2), push(1), push(2), push(5)

​

1. pop() should return 2, as it is the most frequent number

2. Next pop() should return 1

3. Next pop() should return 2

Try it yourself

Try solving this question here:


"""
from heapq import *

class Element:

    def __init__(self, number, frequency, sequenceNumber):
        self.number = number
        self.sequenceNumber = sequenceNumber
        self.frequency = frequency

    def __lt__(self,other):
        # higher frequecy wins
        if self.frequency != other.frequency:
            return self.frequency > other.frequency
        # If both elements have same frequency then return the element that was pushed later
        return self.sequenceNumber > other.sequenceNumber

class FrequencyStack:

      sequenceNumber = 0
      max_stack = []
      count_dict = {}

      def push(self, num):

        # TODO: Write your code here
        self.count_dict[num] = self.count_dict.get(num, 0) + 1
        heappush(self.max_stack, Element(num, self.count_dict[num], self.sequenceNumber))
        self.sequenceNumber += 1

        return 0

      def pop(self):
        num = heappop(self.max_stack).number
        if self.count_dict[num] > 1:
            self.count_dict[num] -= 1
        else:
            del self.count_dict[num]

        return num


def main():
  frequencyStack = FrequencyStack()
  frequencyStack.push(1)
  frequencyStack.push(2)
  frequencyStack.push(3)
  frequencyStack.push(2)
  frequencyStack.push(1)
  frequencyStack.push(2)
  frequencyStack.push(5)
  print(frequencyStack.pop())
  print(frequencyStack.pop())
  print(frequencyStack.pop())


main()







