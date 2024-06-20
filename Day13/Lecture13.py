'''ip:[(1,3) (2,5) (4,6) (6,7) (5,8) (7,9)]
      [5,6,5,4,11,2]
what is the largest amount we can get from all the combinations
op:17'''

'''jo=[(1,3),(2,5),(4,6),(6,7),(5,8),(7,9)]
a=[5,6,5,4,11,2]
b=[5,6,5,4,11,2]
for i in range(1,len(jo)):
    for j in range(0,i):
        if(jo[j][1]<=jo[i][0]):
            if b[j]+a[i]>b[i]:
                b[i]=b[j]+a[i]        
print(max(b))'''
#-----------------------------------------------------------------------

'''ip:s1="abcd"
   s2="axbdc"
op:3'''

'''s1="abcd"
s2="axbdc"
m=[]
for i in range(len(s1)+1):
    l=[0]*(len(s2)+1)
    m.append(l)
for i in range(1,len(s1)+1):
    for j in range(1,len(s2)+1):
        if(s1[i-1]==s2[j-1]):
            m[i][j]=m[i-1][j-1]+1
        else:
            m[i][j]=max(m[i][j-1],m[i-1][j])
print(m[len(s1)][len(s2)])'''

#------------------------------------------------------------------------

'''s1="abcd"
s2="axbdc"
m=[]
u=len(s1)
v=len(s2)
s=""
for i in range(len(s1)+1):
    l=[0]*(len(s2)+1)
    m.append(l)
for i in range(1,len(s1)+1):
    for j in range(1,len(s2)+1):
        if(s1[i-1]==s2[j-1]):
            m[i][j]=m[i-1][j-1]+1
        else:
            m[i][j]=max(m[i][j-1],m[i-1][j])
while(u!=0 and v!=0):
    if(s1[u-1]==s2[v-1]):
        s=s+s1[u-1]
        u=u-1
        v=v-1
    else:
        if(m[u][v]==m[u][v-1]):
            v=v-1
        else:
            u=u-1
print(s[::-1])'''

#---------------------------------------------------------------------------

'''ip:5
   0 1 0 0 1
   1 0 0 1 1
   0 0 0 0 0
   1 0 0 0 0
   1 0 0 0 1
   1-land
   0-water
op:5'''

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
for i in range(n):
    a=[]
    for j in range(n):
        a.append(int(input()))
    l.append(a) 
count=0
for i in range(n):
    for j in range(n):
        if l[i][j]==1:
            count+=1
            fun(l,i,j,n)
print("Number of Islands:",count)'''

#----------------------------------------------------------------------------

'''def fun(l,i,j,n,c): 
    if(i<0 or j<0 or i>=n or j>=n or l[i][j]!=1):
        return c
    if l[i][j]==1:
        l[i][j]=2
    fun(l,i-1,j,n,c)
    fun(l,i,j-1,n,c)
    fun(l,i+1,j,n,c)
    fun(l,i,j+1,n,c)
    return 

n=int(input())
l=[]
for i in range(n):
    a=[]
    for j in range(n):
        a.append(int(input()))
    l.append(a) 
count=0
for i in range(n):
    for j in range(n):
        if l[i][j]==1:
            k=fun(l,i,j,n,0)
            if(k>m):
                m=k
            count+=1
print(count,m)'''
#-------------------------------------------------------------------------

'''ip:7262
op:2 h : 1 m : 2 s
         

l=int(input())
x=l//3600
y=(l%3600)//60
z=l-((3600*x)+(60*y))
print(x,"h",":",y,"m",":",z,"s")'''

'''ip:65476
op:year,month

l=65476
year=l//360
month=(l%360)//30
week=(month)*(30%6)
print(year,month,week)'''





