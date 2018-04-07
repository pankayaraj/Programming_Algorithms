def get_pivot_index(A, low, high):
    p1 = A[low]
    p2 = A[(low+high-1)//2]
    p3 = A[high-1]
    p = p3
    if (p2 > p1 and p2 < p3) or (p2 < p1 and p2 > p3):
        p = p2
    elif p2 > p3 and p2 > p1:
        p = max(p1, p3)
    elif p2 < p1 and p2 < p3:
        p = min(p1, p3)
    return A.index(p)
           
           
    
    
def partition(A,low,high):
    
    j = get_pivot_index(A,low,high)
    pivot = A[j]
    A[low], A[j] = A[j], A[low]
    border = low

    for i in xrange(low+1, high):


        if A[i] < pivot:

            border += 1
            A[i], A[border] = A[border], A[i]
    A[border], A[low] = A[low], A[border]
    return A.index(pivot)

def quicksort(A, low, high):
    if high > low:
        p1 = partition(A, low, high)
        quicksort(A, low, p1)
        quicksort(A, p1+1, high)
        return A
print quicksort(C,0,len(C))
