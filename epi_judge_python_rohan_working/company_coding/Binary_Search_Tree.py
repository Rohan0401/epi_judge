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
    print(pivot)
    for i in range(begin+1, end+1):
        if array[i] <= array[begin]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot

def quicksort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1
    if begin >= end:
        return
    pivot = partition(array, begin, end)
    quicksort(array, begin, pivot-1)
    quicksort(array, pivot+1, end)


if __name__ == '__main__':
    A = [10,5,7,8,4,3]
    quicksort(A)
    print(A)
# int quickSelect(int A[], int l, int h,int k)
# {
#         int p = partition(A, l, h);
#         if(p==(k-1)) return A[p];
#         else if(p>(k-1)) return quickSelect(A, l, p - 1,k);
#         else return quickSelect(A, p + 1, h,k);
#
# }
