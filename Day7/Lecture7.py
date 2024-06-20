#write a program to print all the possible 3 combinations from the list
'''l=[1,2,3,4,5]
x=[]
for i in range(len(l)):
    for j in range(1,len(l)):
        for k in range(2,len(l)):
            x.append((l[i],l[j],l[k]))
print(x)'''
#------------------------------------------------------------
'''def fun(l,k,curr,res):
    if k==3:
        res.append(tuple(curr))
        return
    for i in range(len(l)):
        fun(l,k + 1,curr + [l[i]],res)

l = list(map(int,input().split(',')))
res = []
fun(l, 0, [], res)   
print(res)'''
#------------------------------------------------------------

'''def three_com(l,k):
    def com(curr,start):
        if len(curr)==k:
            print(curr)
            return
        for i in range(start,len(l)):
            com(curr+[l[i]],i+1)
            
        return
    com([],0)
    
l=[3,2,5,6]
r=3
three_com(l,r)'''
#------------------------------------------------------------

'''ip:school
   3
   L 2 ------>hoolsc
   R 3 ------>oolsch
   L 1 ------>chools
hoc
sch,cho,hoo,ool
if hoc is anagram in cho then yes else no

op:yes'''

'''def left_rotate(s,k):
    return s[k:] + s[:k]

def right_rotate(s,k):
    return s[-k:] + s[:-k]

def is_anagram_in_substring(s, target):
    target_sorted = sorted(target)
    for i in range(len(s) - len(target) + 1):
        if sorted(s[i:i+len(target)]) == target_sorted:
            return True
    return False
    
s = "school"

s = left_rotate(s, 2)   
s = right_rotate(s, 3) 
s = left_rotate(s, 1)  
result = is_anagram_in_substring(s, 'hoc')
print("yes" if result else "no")'''
#-------------------------------------------------------------

'''n=input()
l=[('L',2),('R',3),('L',1)]
s=""
for i in range(3):
    if l[i][0]=='L':
        x1=l[i][1]
        s=s+n[x1]
    if l[i][0]=='R':
        x1=l[i][1]
        s=s+n[-x1]
print(s)#hoc'''
#--------------------------------------------------------------

'''a=input()
n=int(input())
str=''
for i in range(n):
    b=input()
    if(b[0]=='L'):
        str=str+a[int(b[2])]
    else:
        str=str+a[-int(b[2])]
print(str)#hoc
str=list(str)
str.sort()#cho
b=[]
for i in range(len(a)-n+1):
    t=list(a[i:n+i])
    t.sort
    b.append(t)
print(b)
print(str)#cho
for i in b:
    if(i==str):
        print("yes")
        break
else:
    print("no")'''
#--------------------------------------------------------
'''ip:12
1 11
2 10
3 9
4 8
5 7
op:yes'''
'''def isprime(x):
    if(x==1):
        return 1
    if(x==2):
        return 1
    for i in range(2,(x//2)+1):
        if(x%i==0):
            return 0
    return 1
a=int(input())
for i in range(1,(a//2)+1):
    if(isprime(i) and isprime(a-i)):
        print("yes")
        break
else:
    print("no")'''
#--------------------------------------------------------
'''ip:2
   polikujmnhytgbyfredcxswqazv
   abbcdd
   op:bbddca
   
   ip:qwryupcsfoghjkldezxvbiintma
   ativedoc
   op:codevita'''
'''n=int(input())
while(n):
    a=input()
    c=input()
    s=''
    for i in a:
        if(i in c):
            s=s+(i*c.count(i))
    print(s)
    n=n-1'''
'''l=[13,9,4,10,5,7]
x=[]
max=0
sum=0
for i in l:
    if i>max:
        max=i
        x.append(max)
        sum=sum+max'''
    
#---------------------------------------------------------  
'''def fun(l):
    if(len(l)==0):
        return 0
    if(len(l)==1):
        return l[0]
    if(len(l)==2):
        return max(l)
    le=l[0]+fun(l[2:])#30
    ri=l[1]+fun(l[3:])#26
    return max(le,ri)#30
l=list(map(int,input().split(',')))
print(fun(l))'''

    
