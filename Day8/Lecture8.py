'''ip:1,2,3,4,1,2,3,1,2
   op:[[1,2,3,4],[1,2,3],[1,2]]
   
   ip:[2,3,1,3,4,3,2]
   op:[[2,3,1,4],[3,2],[3]]
   
   ip:[4,5,2,1]
   op:[[4,5,2,1]]
   
l=[2,3,1,3,4,3,2]
x=[]
c=0
while(c!=len(l)):
    y=[]
    for i in range(len(l)):
        if(not str(l[i]).isalpha()):
            if(l[i] not in y):
                c=c+1
                y.append(l[i])
                l[i]='a'
    x.append(y)
print(x)'''
#-----------------------------------------------

'''l=[2,3,1,3,4,3,2]
d={}
x=[]
c=0
for i in l:
    if(i not in d):
        d[i]=1
    else:
        d[i]=d[i]+1
while(c!=len(l)):'''
#------------------------------------------------------
'''ip:"the quick brown fox jumps over the lazy dog"
op:yes
ip:"qweer yuiop asdfvgh JKL mnbvlkjcxz"
op:no

l="the quick brown fox jumps over the lazy dog"
x=set(l)
if len(x)==27:
    print("yes")
else:
    print("no")'''

'''l="the 4uick @rown f@x jumps over the lazy dogqbo"
x=set(l)
c=0
for i in x:
    if i.islower():
        c=c+1
if c==26:
    print("yes")
else:
    print("no")

x=input()
b="acdefghijklmnopqrstuvwxyz"
for i in x:
    if(i not in b):
        print("no")
        break
else:
    print("yes")
    
x=input()
for i in range(97,123):
    if(i not in b):
        print("no")
        break
else:
    print("yes")'''
#-----------------------------------------------------
#length of longest substring without repeating characters
'''ip:"abfgresagtyuiofde"
7,9,12
op:12'''
'''s="agresgty"
n=len(s)
l=0
maxl=0
x=set()
for r in range(n):
    while s[r] in x:
            x.remove(s[l])
            l+=1
    x.add(s[r])
    maxl= max(maxl,(r- l+ 1))
print(maxl)'''
'''a="abfgresagtyuiofde"
d={}
i=0
s=""
maxl=0
while(i<len(a)):
    while(i<len(a)):
        if(a[i] not in s):
            s=s+a[i]
            d[s[i]]=i
        else:
            if(len(s)>max):
                max=len(s)
            s=""
            break
        i=i+1
    i=d[a[i]]+1
print(max)'''
#---------------------------------------------------------------------------
'''ip:6
   0 1 1 1 0 1
   0 1 0 1 0 0
   1 0 1 1 0 0
   0 0 0 1 1 1
   1 1 0 0 0 1
   1 1 1 0 1 0
   4 6
op:8'''
'''l=[[0,1,1,1,0,1],[0,1,0,1,0,0],[1,0,1,1,0,0],[0,0,0,1,1,1],[1,1,0,0,0,1],[1,1,1,0,1,0]]
n=len(l)
i,j=4,6
def fun(l,i,j,n):
    if l[i][j]==0:
        return
    if l[i][j]==1:
        l[i][j]=0
    if i<n-1:
        fun(l,i+1,j,n)
    if i>0:
        fun(l,i-1,j,n)
    if j<n-1:
        fun(l,i,j+1,n)
    if j>0:
        fun(l,i,j-1,n)
fun(l,4,6,n)
count=0
for i in range(n):
    for j in range(n):
            if l[i][j] == 1:
                count += 1
print(count)'''
#---------------------------------------------------------
'''def fun(l, i, j, n, m):
    if l[i][j] == 0:
        return
    if l[i][j] == 1:
        l[i][j] = 0
    if i < n - 1 and l[i + 1][j] == 1:  
        fun(l, i + 1, j, n, m)
    if i > 0 and l[i - 1][j] == 1:
        fun(l, i - 1, j, n, m)
    if j < m - 1 and l[i][j + 1] == 1:  
        fun(l, i, j + 1, n, m)
    if j > 0 and l[i][j - 1] == 1:  
        fun(l, i, j - 1, n, m)
l = [
    [0, 1, 1, 1, 0, 1],
    [0, 1, 0, 1, 0, 0],
    [1, 0, 1, 1, 0, 0],
    [0, 0, 0, 1, 1, 1],
    [1, 1, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 0]
]
i,j = 3, 5
n=len(l)
m=len(l[0])
fun(l,i,j,n,m)

count = 0
for i in range(n):
    for j in range(m):
        if l[i][j] == 1:
            count += 1
print(count)

def fun(l, i, j,n):
    if (i<0 or j<0 or i>=n or j>=n or  l[i][j] == 0):
        return
    if l[i][j] == 1:
        l[i][j] = 0 
        fun(l, i + 1, j,n)
        fun(l, i - 1, j,n) 
        fun(l, i, j + 1,n)
        fun(l, i, j - 1,n)
l = [
    [0, 1, 1, 1, 0, 1],
    [0, 1, 0, 1, 0, 0],
    [1, 0, 1, 1, 0, 0],
    [0, 0, 0, 1, 1, 1],
    [1, 1, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 0]
]
i,j = 3, 5
n=len(l)
fun(l,i,j,n)

count = 0
for i in range(n):
    for j in range(n):
        if l[i][j] == 1:
            count += 1
print(count)'''
#--------------------------------------------------------

"""
ip: 6
    0 1 1 1 0 1
    0 1 0 1 0 0
    1 0 1 1 0 0 
    0 0 0 1 1 1
    1 1 0 0 0 1 
    1 1 1 0 1 0 
    4 6

op: 8
"""

'''def fun(l,i,j,n): 
    if(i<0 or j<0 or i>=n or j>=n or l[i][j]!=1):
        return
    if l[i][j]==1:
        l[i][j]=2
    fun(l,i-1,j,n)
    fun(l,i,j-1,n)
    fun(l,i+1,j,n)
    fun(l,i,j+1,n)
    return 
n=int(input())
l=[]
co=0
for i in range(n):
    l1=[]
    for j in range(n):
        l1.append(int(input()))
    l.append(l1)
r=int(input())
c=int(input())  
fun(l,r-1,c-1,n) 
for i in range(n):
    for j in range(n):
        if l[i][j]==1:
            co=co+1
print(l)
print("Trees:",co)'''
#----------------------------------------------------------
'''ip:4
 t u e d
 f b o w
 r o o k
 d r k i
 book
op:yes

def fun(i,j,k,t):
    if(len(s)):
        return 1
    if(i<0 or j<0 or i>=n or j>=n or a[i][j]!=s[k]):
        return
    if(a[i][j]==s[k]):
        a[i][j]=0
    t=fun(i+1,j,k+1)
    t=fun(i-1,j,k+1)
    t=fun(i,j-1,k+1)
    t=fun(i,j+1,k+1)
    return t'''

#-----------------------------******TREES******---------------------------------
class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class tree:
    def __init__(self):
        self.root=None
    def create(self,root,x):
        if(root==None):
            self.root=node(x)
        elif(root.data>x):
            self.create(root.left,x)
        else:
            self.create(root.right,x)
t1=tree()
t1.create(t1.root,10)
t1.create(t1.root,5)
t1.create(t1.root,20)
t1.create(t1.root,7)
t1.create(t1.root,1)
            
    
    
        
       




    
    
    
    
    


    
    


    