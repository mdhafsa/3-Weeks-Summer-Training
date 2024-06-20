'''ip:
    khoor
    3
op:hello

ip:bcdmnwc
    9
    student

ip:bvec
4
op:xray

a=input()
b=input()
steps=int(b)%26
res=''
for i in a:
    if((ord(i)-steps)>=97):
        res=res+chr(ord(i)-steps)
    else:
        res=res+chr(ord(i)-steps+26)
print(res)'''
'''ip:xyzabcdefklmnopqefgh
a=input()
n=len(a)
c=1
m=0
for i in range(n-1):
    if((ord(a[i])+1)==ord(a[i+1])):
        c=c+1
    else:
        if(c>m):
            m=c
        c=1
if(c>m):
    m=c
print(m)
-----------------------------------------------------------------
ip:3
   xyz
   pqr
   abc
   "yraxpazr"
op:
    yes

4
abcd
xyze
pqrw
stuv
"cyptdzsayq"
op:
    no

n =int(input())
m=[]
for i in range(n):
    row=list(input())
    m.append(row)
s=input()
f=0
for i in range(len(s)):
    if s[i] not in m[i%n]:
        print("no")
        break
    else:
        m[i].remove(s[i])
if(f==0):
    print("yes")'''
#---------------------------------------------------------------------
'''def palindrome(n,rev):
    if n<=0:
        return rev
    else:
        r=n%10
        rev=(rev*10)+(r)
        return palindrome(n//10,rev)
n=int(input())
rev=0
if(n==palindrome(n,rev)):
    print("Palindrome")
else:
    print("Not Palindrome")'''
#------------------------------------------------------------------------

'''ip:5
op:
    * * * * *
    * 1 2 3 *
    * 4 5 6 *
    * 7 8 9 *
    * * * * *
n=int(input())
k=1
for i in range(n):
    for j in range(n):
        if ((i==0 or j==0) or (i==n-1 or j==n-1)):
            print("*",end=" ")
        else:
            print(k,end=" ")
            k=k+1
    print()
#-------------------------------------------------------------------------
ip:4
----a----
---aba---
--abcba--
-abcdacba-
a=int(input())
for i in range(a+1):
    for j in range(a+1-i):
        print(' ',end='')
    for j in range(1,i+1):
        print('%c'%(a+j),end='')
    for j in range(i-1,0,-1):
        print('%c'%(a+j),end='')
    print()'''
        
        
        
        
        
    
    

        
        
    





        

    
    



 
    
    

    
    
    
    
    
