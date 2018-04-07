#reference  https://www.youtube.com/watch?v=13m9ZCB8gjw
# CODE TO FIND THE LOWEST COMMON ANCESTOR(in other word the futherest comman parent of the original root)
# Runs in a complexity of O(n)

#Every node is inserted as the rightchild and left child after making them as a tree
#A string value is given to the root
#if possible finnd a better repesentation for the tree
class BinaryTree:
    def __init__(self,root):
        self.key            = root
        self.left_child     = None
        self.right_child    = None

    def insert_left(self,new):
        if self.left_child == None:
            
            self.left_child = BinaryTree(new)
        else:
            t = BinaryTree(new)
            t.left_child  = self.left_child
            self.left_child = t

    def insert_right(self, new):
        if self.right_child == None:
            
            self.right_child = BinaryTree(new)
        else:
            t = BinaryTree(new)
            t.right_child = self.right_child
            self.right_child = t


    def get_left_child(self):
        return self.left_child


    def get_right_child(self):
        return self.right_child


    def set_root_val(self,object):
        self.key = object

    def get_root_val(self):
        return self.key

#Note : A function terminates at the return command if it happens the rest of the code won't happen
    
    


def LCA(root,n1,n2):

    # If the given root doesn't exist
    if root == None:
        return None
    #else if the either of them is a
    if root.key == n1:
        return n1

    if root.key == n2:
        return n2

    for_l_child = LCA(root.left_child,n1,n2)
    for_r_child = LCA(root.right_child,n1,n2)

    #if both the children are n1 and n2 then this must be the LCA
    if for_l_child and for_r_child:
        return root.key

    #if both are None that means the root terminates with that node
    if for_l_child == None and for_r_child == None:
        return None

    #if the above conditions doessn't apply
    if for_l_child != None:
        return for_l_child
    else:
        return for_r_child

A = BinaryTree('A')






A.insert_left('B')
A.insert_right('C')
A.right_child.insert_left('H')
A.right_child.left_child.insert_left('I')
A.left_child.insert_right('D')
A.left_child.insert_left('E')
A.left_child.left_child.insert_right('F')
A.left_child.left_child.insert_left('G')

print LCA(A,'E','G') #ans E
print LCA(A,'A','I') #ans A
print LCA(A,'C','F') #ans A
print LCA(A,'G','I') # ans A 
