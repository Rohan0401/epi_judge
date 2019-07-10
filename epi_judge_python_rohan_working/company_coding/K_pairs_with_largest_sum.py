from heapq import *
def find_k_largest_pairs(nums1, nums2, k):
  result = []
  minHeap = []
  # TODO: Write your code here
  for i in range(0 , min(k , len(nums1))):
      for j in range(min(k, len(nums2))):
          if len(minHeap) < k:
              heappush(minHeap, (nums1[i] + nums2[j] , i, j))
          else:
              if nums1[i] + nums2[j] < minHeap[0][0]:
                break

              else:
                  heappop(minHeap)
                  heappush(minHeap, (nums1[i] + nums2[j], i , j))
  print(minHeap)
  for (diff, i, j) in minHeap:
      result.append([nums1[i],nums2[j]])

  return result


def main():
  print("Pairs with largest sum are: " +
        str(find_k_largest_pairs([9, 8, 2], [6, 3, 1], 3)))


main()
