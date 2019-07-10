
def find_Kth_smallest(matrix, k):
    n = len(matrix)
    start, end = 0, matrix[n-1][n-1]
    while start < end:
        mid = start + (end - start) / 2
        # set both smaller and larger be the first and last number
        smaller, larger = matrix[0][0], matrix[n-1][n-1]
        count, smaller, larger = find_count(matrix, mid, smaller, larger)

        if count == k:
            return smaller
        elif count < k:
            start = larger
        else:
            end = smaller
    return start

def find_count(matrix, mid, smaller, larger):

    count = 0
    n = len(matrix)
    row, col = n -1, 0

    while row >= 0 and col < n:
        if matrix[row][col] > mid:
            larger = min(larger, matrix[row][col])
            row -= 1
        else:
            smaller = max(smaller, matrix[row][col])
            count += row + 1
            col += 1

    return count, smaller, larger






    return number


def main():
  print("Kth smallest number is: " +
        str(find_Kth_smallest([[2, 6, 8], [3, 7, 10], [5, 8, 11]], 5)))


main()
