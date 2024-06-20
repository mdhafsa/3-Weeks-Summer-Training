'''def adds(n):
    s=0
    while(n):
        s=s+n%10
        n=n//10
    return s  
def pnp(n):
    if(n in [2,3,5,7]):
        return m
    else:
        return m+1
n=int(input())
m=n
if(n<10):
    print(pnp(n))
else:
    while(1):
        n=adds(n)
        if(n<10):
            break
    print(pnp(n))'''
#-------------------------------------------------------------------------
    
'''a=[3,8,5,4,3]
b=[5,0,9,3,2]
(12,17)'''

'''def sum(i,s1,s2):
    
a=[3,8,5,4,3]
b=[5,0,9,3,2]   '''
'''x=13
def sum(x):
    if x==0:
        return 0
    return x+sum(x-2)
if x%2==0:
    print(sum(x))
else:
    print(sum(x-1))'''
#-------------------------------------------------------------------------

'''difference between leftsum and rightsum
n=[10,4,8,3]
b=[]
for i in range(len(n)):
    print(abs(sum(n[:i])-sum(n[i+1:])))
   (or)
n=[10,4,8,3]
s=sum(n)
x=0
j=0
for i in n:
    n[j]=abs((x)-(s-i-x))
    x=x+1
    j=j+1
print(n)'''

#--------------------------------------------------------------------------

'''a="MMFFF"
c=0
for i in a:
    if(i=='M'):
        c+=1
    else:
        c-=1
if c==0:
    print(0)
elif c>1:
    print('M')
else:
    print('F')'''
#-----------------------------------------------------------------------------
'''s="leet*code"
st=[]
for i in s:
    if i!='*':
        st.append(i)
    else:
        st.pop()
print(''.join(st))'''
#----------------------------------------------------------------------------
'''
ip:is2 sentence4 This1 a3
op:This is a statement
a="is2 sentence4 This1 a3"
a=a.split()
res=[0]*len(a)
for i in a:
    res[int(i[-1])-1]=i[:-1]
print(' '.join(res))  '''     
    
        

    