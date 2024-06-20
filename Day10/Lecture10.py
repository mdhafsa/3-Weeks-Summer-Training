'''ip:[4,8,14,22,36,68]
   7+13+19+31+67
   op:137
   
   [14,16,20,22]
   0+19+0
   op:19'''
'''def isprime(x):
    for i in range(2,(x//2)+1):
        if(x%i==0):
            return 0
    return 1
#-------------------------------------------------------------      
def largest_prime(n,m):
    for i in range(m-1,n,-1):
        if(isprime(i)):
            return i
    return 0
    
l=[4,8,14,22,36,68]
s=0
for i in range(0,len(l)-1):
    s=s+largest_prime(l[i],l[i+1])
print(s)'''
#-----------------------------------------------------------

'''ip:[4,9,8,2,14,3,5,6]
op:[4,2,8,3,5,6,9,14]

l=list(map(int,input().split()))
for i in range(len(l)-2):
    if(l[i]>l[i+1]):
        l[i],l[i+1]=l[i+1],l[i]
    if(l[i+1]>l[i+2]):
        l[i+1],l[i+2]=l[i+2],l[i+1]
    if(l[i]>l[i+1]):
        l[i],l[i+1]=l[i+1],l[i]
print(l)'''
#-----------------------------------------------------------

'''ip:"hello:5438,car:214,book:8799,apple:2187"
op:oaxp'''

'''def char(word,num):
    length=len(word)
    while length>0:
        if str(length) in num:
            return word[length-1]
        length-=1
    return 'x'

s = "hello:5438,car:214,book:8799,apple:2187"
pairs= s.split(',')
result = []
for i in pairs:
    word,num = i.split(':')
    result.append(char(word,num))
    
x= ''.join(result)
print(x)'''
#--------------------------------------------------------

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
    def leftview(self,root,c,l):
        if(root==None):
            return []
        if c >=len(l):
            l.append((root.data,c))
        self.leftview(root.left,c+1,l)
        self.leftview(root.right,c+1,l)
        return l
    def rightview(self,root,c,l):
        if(root==None):
            return []
        if c >=len(l):
            l.append((root.data,c))
        self.rightview(root.right,c+1,l)
        self.rightview(root.left,c+1,l)
        return l
    def topview(self,root):
        if(root==None):
            return
        d={}
        q=[(root,0)]
        while(q):
            root=q[0][0]
            if(root.left!=None):
                q.append((root.left,q[0][1]-1))
            if(root.right!=None):
                q.append((root.right,q[0][1]+1))
            if(q[0][1] not in d):
                d[q[0][1]]=root.data
            q.pop(0)
        for i in sorted(d):
            print(d[i],end=" ")
    def bottomview(self,root):
        if(root==None):
            return
        d={}
        q=[(root,0)]
        while(q):
            root=q[0][0]
            if(root.left!=None):
                q.append((root.left,q[0][1]-1))
            if(root.right!=None):
                q.append((root.right,q[0][1]+1))
            d[q[0][1]]=root.data
            q.pop(0)
        for i in sorted(d):
            print(d[i],end=" ")
                   
t1 = tree()
t1.root = t1.create(t1.root, 10)
t1.create(t1.root, 5)
t1.create(t1.root, 20)
t1.create(t1.root, 7)
t1.create(t1.root, 1)
print(t1.leftview(t1.root,0,[]))
print(t1.rightview(t1.root,0,[]))       
t1.topview(t1.root)
print()
t1.bottomview(t1.root)    
        


