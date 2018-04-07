# Euclidian method to find the greatest common diviser
# reference :https://www.topcoder.com/community/data-science/data-science-tutorials/mathematics-for-topcoders/

def GCU(a,b):
    if a == b:
        return a
    else:
        if a > b:
            x = b
            y = a
        elif  a <  b:
            x = a
            y = b
    

        rem  = x
        while rem != 0:
            
            rem = y%x
            y = x
            x = rem

        return y


print GCU(2336,1314)        
