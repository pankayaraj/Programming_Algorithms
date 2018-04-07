def get_pivot(A, low, high):
    return A.index(A[high-1])
def partition(A, low, high):
    p = get_pivot(A,low,high)
    V = A[p]
    j = low
    for i in xrange(low,high):
        if A[i] < V:

            A[i], A[j] = A[j], A[i]
            j += 1
    A[j] , A[p] = A[p], A[j]
    print ' '.join(map(str,A))
    return A.index(V)

def quicksort(A,low,high):
    if high-1 > low:
        a = partition(A,low,high)
        quicksort(A,low,a)
        quicksort(A,a+1,high)
n = int(raw_input())
A = map(int,raw_input().strip().split())
quicksort(A,0,len(A))






