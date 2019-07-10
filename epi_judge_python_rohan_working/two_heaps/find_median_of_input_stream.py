from heapq import *
class MedianOfAStream:

  def __init__(self):
      self.maxHeap = [] # Contain the first half of elements
      self.minHeap = [] # Contain the second half of elements

  def insert_num(self, num):
   # TODO: Write your code here
   # insert into max heap

   if not self.maxHeap or -self.maxHeap[0] >= num:
       heappush(self.maxHeap, -num)
   else:
       heappush(self.minHeap, num)

   # either obth heap will have same number of element of maxHeap has more element

   if len(self.maxHeap) > len(self.minHeap) + 1:
       heappush(self.minHeap, -heappop(self.maxHeap))
   elif len(self.maxHeap) < len(self.minHeap):
       heappush(self.maxHeap, -heappop(self.minHeap))


  def find_median(self):
    # TODO: Write your code here

    if len(self.minHeap) == len(self.maxHeap):
        return -self.maxHeap[0] / 2.0 + self.minHeap[0] / 2.0

    return -self.maxHeap[0] / 1.0



def main():
  medianOfAStream = MedianOfAStream()
  medianOfAStream.insert_num(3)
  medianOfAStream.insert_num(1)
  print("The median is: " + str(medianOfAStream.find_median()))
  medianOfAStream.insert_num(5)
  print("The median is: " + str(medianOfAStream.find_median()))
  medianOfAStream.insert_num(4)
  print("The median is: " + str(medianOfAStream.find_median()))


main()
