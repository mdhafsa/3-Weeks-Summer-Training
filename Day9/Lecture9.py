class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class tree:
    def __init__(self):
        self.root = None

    def create(self,root,x):
        if root==None:
            return node(x)
        else:
            if root.data>x:
                root.left = self.create(root.left, x)
            else:
                root.right = self.create(root.right, x)
        return root
    
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.data,end=" ")
            self.inorder(root.right)

    def preorder(self,root):
        if root:
            print(root.data,end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self,root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data,end=" ")
            
    def sumofnodes(self,root):
        if root==None:
            return 0
        else:
            left=self.sumofnodes(root.left)
            right=self.sumofnodes(root.right)
            return root.data+left+right
        
    def evensum(self,root):
        if root==None:
            return 0
        s=0
        if(root.data%2==0):
            s=s+root.data
        s=s+self.evensum(root.left)
        s=s+self.evensum(root.right)
        return s
    
    def evensum1(self,root):
        if root==None:
            return 0
        if root.data%2==0:
            return root.data+self.evensum1(root.left)+self.evensum1(root.right)
        else:
            return self.evensum1(root.left)+self.evensum1(root.right)
        
    def diff_even_odd(self,root):
        if root==None:
            return 0
        if(root.data%2==0):
            return root.data+self.diff_even_odd(root.left)+self.diff_even_odd(root.right)
        else:
            return self.diff_even_odd(root.left)+self.diff_even_odd(root.right)-root.data
        
    def height(self,root):
        if root==None:
            return -1
        left_height=self.height(root.left)
        right_height=self.height(root.right)
        return max(left_height,right_height) + 1
    
    def balancedtree(self,root):
        return abs(self.height(root.left)-self.height(root.right))<=1
    
    def check_leafnode(self,root):
        if root==None:
            return 0
        if root.left==None and root.right==None:
            return 1
        return self.check_leafnode(root.left) + self.check_leafnode(root.right)
    
    def sum_leafnodes(self,root):
        s=0
        if root==None:
            return 0
        if root.left==None and root.right==None:
            s=s+root.data
        s=s+self.sum_leafnodes(root.left)
        s=s+ self.sum_leafnodes(root.right)
        return s
    
    def search_node(self,root,x):
        if root==None:
            return 0
        if root.data==x:
            return 1
        elif x<root.data:
            return self.search_node(root.left,x)
        else:
            return self.search_node(root.left,x)
        
    def depth(self,root,x):
        if root==None:
            return -1
        if root.data==x:
            return 0
        elif root.data<x:
            return 1+self.depth(root.right,x)
        else:
            return 1+self.depth(root.left,x)
    
        
        
               
t1 = tree()
t1.root = t1.create(t1.root, 10)
t1.create(t1.root, 5)
t1.create(t1.root, 20)
t1.create(t1.root, 7)
t1.create(t1.root, 1)
t1.inorder(t1.root)
print()
t1.preorder(t1.root)
print()
t1.postorder(t1.root)
print()
print("sum of all nodes in a tree:",t1.sumofnodes(t1.root))
print("absolutediff bwt left and right subtree:",abs((t1.sumofnodes(t1.root.left))-(t1.sumofnodes(t1.root.right))))
print("evensum:",t1.evensum(t1.root))
print(t1.evensum1(t1.root))
print("difference of even and odd:",t1.diff_even_odd(t1.root))
print("Height of the tree:",t1.height(t1.root))
if(t1.balancedtree(t1.root)):
    print("balanced")
else:
    print("not balanced")
print(t1.check_leafnode(t1.root))
print(t1.sum_leafnodes(t1.root))
print(t1.search_node(t1.root,1))
print(t1.search_node(t1.root,12))
print(t1.depth(t1.root,1))