# coin change problem
# solution considering overlapping sub problems
# reference : http://www.geeksforgeeks.org/dynamic-programming-set-7-coin-change/
# coins : no of change available, n : amount , m = len(coins)

def coin(coins,n,m):
    T = [[0 for  i in xrange(n+1)]for j in xrange(m)]
    
    for i in xrange(m):
        T[i][0] = 1 #for n = 0 returning 1

    for i in xrange(1,n+1):
        for j in xrange(m):
            
            if j >= 1:
                x = T[j-1][i]

            else:
                x = 0

            if i- coins[j] >= 0:
                y = T[j][i-coins[j]]
            else:
                y = 0
       
            T[j][i] = x + y

    return T[m-1][n]

'''
coins = [1,2,3]
print coin(coins,4,3)

coins = [2,5,3,6]
print coin(coins,10,4)
''''
