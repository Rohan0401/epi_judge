def search_triplets(arr):
  arr.sort()
  triplets = []
  for i in range(len(arr)):
    if i > 0 and arr[i] == arr[i-1]:  # skip same element to avoid duplicate triplets
      continue
    search_pair(arr, -arr[i], i+1, triplets)

  return triplets


def search_pair(arr, target_sum, left, triplets):
  right = len(arr) - 1
  while(left < right):
    current_sum = arr[left] + arr[right]
    if current_sum == target_sum:  # found the triplet
      triplets.append([-target_sum, arr[left], arr[right]])
      left += 1
      right -= 1
      while left < right and arr[left] == arr[left - 1]:
        left += 1  # skip same element to avoid duplicate triplets
      while left < right and arr[right] == arr[right + 1]:
        right -= 1  # skip same element to avoid duplicate triplets
    elif target_sum > current_sum:
      left += 1  # we need a pair with a bigger sum
    else:
      right -= 1  # we need a pair with a smaller sum


def main():
  print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
  print(search_triplets([-5, 2, -1, -2, 3]))

if __name__ == '__main__':
    main()

# If we know the length of the LinkedList cycle, we can find the start of the cycle through the following steps:
#
# Take two pointers. Let’s call them pointer1 and pointer2.
# Initialize both pointers to point to the start of the LinkedList.
# We can find the length of the LinkedList cycle using the approach discussed in LinkedList Cycle. Let’s assume that the length of the cycle is ‘K’ nodes.
# Move pointer2 ahead by ‘K’ nodes.
# Now, keep incrementing pointer1 and pointer2 until they both meet.
# As pointer2 is ‘K’ nodes ahead of pointer1, which means, pointer2 must have completed one loop in the cycle when both pointers meet. Their meeting point will be the start of the cycle.
