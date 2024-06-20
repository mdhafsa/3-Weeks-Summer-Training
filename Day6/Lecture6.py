'''print the number whose frequency is half of the more than the length of the list
l=[4,8,2,4,4,8,4]
max=0
p=0
for i in l:
    if(l.count(i)>max):
        max=l.count(i)
        p=i
print(p)
(or)
a=list(map(int,input().split(',')))
c=1
p=a[0]
for i in range(1,len(a)):
    if(a[i]==p):
        c=c+1
    else:
        c=c-1
        if(c==0):
            c=1
            p=a[i]
print(p)'''
#-----------------------------------------------------
'''print the missing number
l=[0,2,3,4,5]
x=len(l)
b=sum(l)
x=(x*(x+1))//2
print(x-b)'''
#-------------------------------------------------------
'''n=int(input())
k=int(input())
f=[]
x=0
for i in range(1,n+1):
        if n%i==0:
            f.append(i)
s=sorted(f,reverse=True)
print(s[k-1])
(or)
n=int(input())
k=int(input())
c1=0
c=0
if k==1:
    print(k)
else:
    for i in range(1,n+1):
        if n%i==0:
            c1=c1+1
for i in range(1,n+1):
    if n%i==0:
        c=c+1
        if c==(c1-(k+1)):
            print(i)'''
#------------------------------------------------------

'''n=int(input())
m=int(input())
for i in range(2,(min(n,m)//2)+1):
     if(n%i==0 and m%i==0):
         print(not co primes)
         break
else:
   print(prime)
'''
#--------------------------------------------------
'''The given string is balanced or not
import math
a=5
b=4
print(math.gcd(a,b))'''
'''x=input()
s=[]
for i in range(len(x)):
    if x[i]=="(" or x[i]=='[' or x[i]=='{':
        s.append(i)
    elif x[i]==']' and s[-1]=='[':
        s.pop()
    elif x[i]=='}' and s[-1]=='{':
        s.pop()
    elif x[i]==')' and s[-1]=='(':
        s.pop()
    else:
        print(i,"not balanced")
if(len(s)==0):
    print("balanced")'''

    