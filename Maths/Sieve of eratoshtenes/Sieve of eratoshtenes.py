#sieve of eratosthenes
def find_prime_no(n):
    j = 0
    L = range(2,n+1)
    while True:
        if len(L)> j:
            a = L[j]
            
            for i in xrange(j+1,len(L)):
                if i < len(L):
                           
                    if L[i]%a == 0:
                        L.remove(L[i])
                    
            j += 1    
        else:
            
            return len(L)+1
            break
    
#sieve of eratosthenes2
def find_prime_no(n):
    P = [1]*(n+1)
    numbers = 0
    for i in xrange(2,n+1):
        if P[i] == 1:
            numbers += 1
            j = i**2
            while j <= n:
                P[j] = 0
                j += i
    return numbers
