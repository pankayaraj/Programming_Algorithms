from operator import itemgetter
def closest_pair(L):
    L.sort()
    n = len(L)
    p = n//2
    d1 = float('inf')
    
    for i in xrange(n//2-1):
        for j in xrange(i+1,n//2):
            a = pow((L[j][0] - L[i][0])**2 + (L[j][1] - L[i][1])**2,0.5)
            if a < d1:
                d1 = a
                #point1 = [L[i],L[j]]

    d2 = float('inf')
     
    for i in xrange(n//2,n-1):
        for j in xrange(i+1,n):
            a = pow((L[j][0] - L[i][0])**2 + (L[j][1] - L[i][1])**2,0.5)
            if a < d2:
                d2 = a
                #point2 = [L[i],L[j]]

                
    if d1 < d2:
        d = d1
        #point = point1
    else:
        d = d2
        #point = point2
        
    
    L2 = []
    x = L[n//2][0]-d
    
    for i in xrange(n//2-1,-1,-1):
        if L[i][0] > x:
           
            L2.append(L[i])
        else:
            break

    x = L[n//2][0] + d
    
    for i in xrange(n//2,n):
        if L[i][0] < x:
            L2.append(L[i])
        else:
            break

    L2.sort(key = itemgetter(1))
    ans = d
    
    for i in  xrange(len(L2)-1):
        z = min(len(L2)-i,7)
        for j in xrange(i+1,i+z):
            
            a = pow((L2[j][0] - L2[i][0])**2 + (L2[j][1] - L2[i][1])**2,0.5)
            if ans > a:
                ans = a
                #point = [L2[i],L2[j]]
    
    return ans #,point
            
        
    
        
        
L = [[2,3], [12,30], [40,50], [12,10], [3,4]]
print closest_pair(L)

