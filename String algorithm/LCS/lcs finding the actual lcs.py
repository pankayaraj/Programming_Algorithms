 
def lcs(X , Y):
    
    m = len(X)
    n = len(Y)
 
    
    L = [[None]*(n+1) for i in xrange(m+1)]
 
    
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0 :
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                if L[i-1][j] > L[i][j-1]:
                                    
                    L[i][j] = L[i-1][j]
                else:
                    L[i][j] = L[i][j-1]
                                    
                                    
    
    return L
L =  lcs(A,B)
m = len(A)
n = len(B)

i = m
j = n
S = []
while i > 0 and j > 0:
    
   
    if A[i-1] == B[j-1]:
        S.append(A[i-1])
        i -= 1
        j -= 1
    else:
        if L[i-1][j] > L[i][j-1]:
            i -= 1
        else:
            j -= 1

print S
