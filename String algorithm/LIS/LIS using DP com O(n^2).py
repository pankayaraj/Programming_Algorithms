# Longest increasing subsequence length using dynamic programinng
# Time complexity is O(n^2)
# reference = http://www.geeksforgeeks.org/dynamic-programming-set-3-longest-increasing-subsequence/
def LIS(array):
    n = len(array)

    L = [1]*n # creates an array that stores the LIS length in an array

    for i in xrange(1,n):
        for j in xrange(i):
            if array[i] > array[j]:
                if L[i] < L[j]+1:
                    L[i] = L[j]+1
        ans = 0
    for i in xrange(n):
        if L[i] > ans:
            ans = L[i]

    return ans

'''
array = [10, 22, 9, 33, 21, 50, 41, 60]
print LIS(array)
'''
