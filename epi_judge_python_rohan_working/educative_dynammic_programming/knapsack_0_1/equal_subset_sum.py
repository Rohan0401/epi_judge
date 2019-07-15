def can_partition(num):
  # TODO: Write your code here
  s = sum(num)
  # check if the sum is even or odd
  if s%2 != 0:
      return False

  return can_partition_recursive(num, s//2, 0)







  return False

def can_partition_recursive(num, sum, currentIndex):

    #base case
    if sum == 0 :
        return True

    n = len(num)

    if currentIndex >= n or n == 0:
        return False

    # recurse the number if the dum does not exceeds the number

    if num[currentIndex] <= sum:
        if can_partition_recursive(num, sum - num[currentIndex], currentIndex+1):
            return True
    #  recuresive call after exclusing the number
    return can_partition_recursive(num, sum, currentIndex+1)


    return dp
def main():
  print("Can partition: " + str(can_partition([1, 2, 3, 4])))
  print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))
  print("Can partition: " + str(can_partition([2, 3, 4, 6])))


main()
