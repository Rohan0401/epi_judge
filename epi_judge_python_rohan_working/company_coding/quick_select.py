##
## Quick sort algo
# [1,5,7,8,4,3]
# Pick a random pivot
"""
Partition algorithm (using Lomuto partition scheme)

algorithm partition(A, lo, hi) is
    pivot := A[hi]
    i := lo        // place for swapping
    for j := lo to hi – 1 do
        if A[j] ≤ pivot then
            swap A[i] with A[j]
            i := i + 1
    swap A[i] with A[hi]
    return i
Quicksort algorithm (using Lomuto partition scheme)

algorithm quicksort(A, lo, hi) is
    if lo < hi then
        p := partition(A, lo, hi)
        quicksort(A, lo, p – 1)
        quicksort(A, p + 1, hi)
"""


def partition(array, begin, end):
    pivot = begin
    for i in range(begin + 1, end + 1):
        if array[i] <= array[begin]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot


def quickselect(array, begin=0, end=None, k=3):

    if end is None:
        end = len(A) - 1
    if begin >= end:
        return
    pivot = partition(array, begin, end)
    if pivot == (k - 1):
        return A[pivot]
    elif pivot > k - 1:
        return quickselect(A, begin, pivot - 1, k)
    else:
        return quickselect(A, pivot + 1, end, k)


if __name__ == '__main__':
    A = [10, 5, 7, 8, 4, 3]
    a = quickselect(A)
    print(a)
    print(A)

# int quickSelect(int A[], int l, int h,int k)
# {
#         int p = partition(A, l, h);
#         if(p==(k-1)) return A[p];
#         else if(p>(k-1)) return quickSelect(A, l, p - 1,k);
#         else return quickSelect(A, p + 1, h,k);
#
# }
