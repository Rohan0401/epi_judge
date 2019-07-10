from random import randint
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
         n = len(arr)
         left = 0
         right = n - 1

         while (left <=right):
             pivot = randint(left, right)

             final_position = self.partition(arr, left, right , pivot)

             if final_position == n - k:
                 return arr[final_position]
             elif (final_position > n -k ):
                 right = final_position - 1
             else:
                 left final_position + 1
         return -1

    def partition(self, arr, left, right, pivot):
        pivot_val = arr[pivot]

        lesser_iter = left

        arr[pivto], arr[right] = arr[right], arr[pivot]

        for i in range(left, right):

            if arr[i] < pivot_value:
                arr[i], arr[lesser_item] = arr[lesser_iter], arr[i]
                lesser_iter += 1
         arr[lesse_item], arr[right] = arr[right], arr[lesser_item]

         return lesser_item
