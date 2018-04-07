
def bubble_sort(list):
    
    exchange  = True
    for num_pass in xrange(len(list)-1,0,-1):
        
        if exchange != True:
            
            break
            
        exchange = False
        for  ab in xrange(num_pass):
            if list[ab] > list[ab+1]:
                list[ab],list[ab+1] = list[ab+1],list[ab]
                exchange = True
    return list

