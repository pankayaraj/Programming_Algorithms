from math import *
#reference : WIKEPEDIA


#to obtain the left and right child index of a node
def find_leftchild(i):
    return 2*i+1
def find_rightchild(i):
    return 2*i+2

#to get the parent index of a given node
def find_parent(i):
    return (i-1)//2
    
#functiom to select a child and bring him to the right position on the top
#here end represents the child and start says how much can he move i.e the parental limit
#complexity: nlog(n)
def shiftup(array,start,end):
    child = end
    parent = find_parent(child)

    while parent > start: #the parental limit is preserved
        parent = find_parent(child)
        if array[parent] < array[child]:
           array[parent],array[child] = array[child],array[parent]
           child = parent    #makes the parent as the next child and check the heap
        else:
            
            return array
            break
    else:
        return array
    


#to create a heap using for an array
# this function returns a maxheap(the parent has the higest value comapred to the child
def heapify(array,length):
    end = 1 #start from the foremost left child and move on

    while end > length:
        array = shiftup(array,start,end)
        end += 1 #do the same procedure 
    





    
    
    
        
