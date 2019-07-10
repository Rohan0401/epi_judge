def dutch_flag_sort(arr):
  # TODO: Write your code here
  low, high = 0, len(arr) - 1
  i = 0

  while i <= high:
      if arr[i] == 0:
          arr[i], arr[low] = arr[low], arr[i]
          i += 1
          low += 1
      elif arr[i] == 1:
          i += 1
      else:
          arr[i], arr[high] = arr[high], arr[i]
          high -= 1


  return arr

def main():
  arr = [1, 0, 2, 1, 0]
  dutch_flag_sort(arr)
  print("This is soerted array: ",arr)

  arr = [2, 2, 0, 1, 2, 0]
  dutch_flag_sort(arr)
  print("This is soerted array: ",arr)


main()
