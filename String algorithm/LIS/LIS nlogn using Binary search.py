#Longest increasing subsequence time complexity nlogn
# using binary search



def binarySearch(array,t, l, r, x):
 
    while l+1 < r: 
        mid = l + (r - l)/2
       
        if array[t[mid]] < x:
            l = mid 
         
        else:
            r = mid
     
    
    return r

def LIS(array):
    n = len(array)
    ans = 1
    tem = [0]
    trac = [-1]*n # tracker to get the LIS

    for i in xrange(1,n):
        
        if array[i] > array[tem[-1]]:
            tem.append(i)
            ans += 1
        elif array[i] < array[tem[0]]:
            tem[0] = i

        else:
            p = binarySearch(array,tem, -1, len(tem)-1, array[i]) #excessive testcases are running with only -1 so keep it
            tem[p] = i
    '''
    #incase if u want the lis
    lis = []
    for i in xrange(ans):
        lis.append(array[tem[i]])
    '''    
    
    
    return ans#,lis

'''
array = [1,5,10,3,2,6,8]
print LIS(array)
print array            
'''            

    
