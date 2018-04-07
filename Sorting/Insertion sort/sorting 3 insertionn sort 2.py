#!/bin/python
def insertionSort(ar):    
    a = len(ar)
    
    for i in xrange(1,a):
        
        V = ar[i]
        k = i
        
        while V < ar[k-1] and k-1 != -1:
            ar[k] = ar[k-1]
            ar[k-1] = V
            k -= 1
        print ' '.join(map(str,ar))
            
            
        
        

m = raw_input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
