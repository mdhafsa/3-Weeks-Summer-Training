'''1.Merge two sorted lists two make one sorted list
l1=[2,5,7,9]
l2=[1,3,6,7,10,13]
l3=[]
i,j=0,0
while(i<len(l1) and j<len(l2)):
    if(l1[i]<l2[j]):
        l3.append(l1[i])
        i=i+1
    else:
        l3.append(l2[j])
        j=j+1
if(j<len(l2)):
    l3.extend(l3[j:])
if(i<len(l1)):
    l3.extend(l3[i:])
print(l3)
----------------------------------------------------
2. ip:aaabbaaaaddd
   op:a3b2a4d3

l1="aaabbaaaaddd"
c=1
l2=''
for i in range(len(l1)-1):
    if(l1[i]==l1[i+1]):
        c=c+1
    else:
        l2=l2+l1[i]+str(c)
        c=1
l2=l2+l1[-1]+str(c)
print(l2) 
---------------------------------------------------
3. ip:3 5 4 3 6 7 1 2 4 3 3 7 6
   op:3 - 4
      5 - 1
      4 - 2
      6 - 2
      7 - 2
      1 - 1
      2 - 1
a=[3,5,4,3,6,7,1,2,4,3,3,7,6]
b=[]
for i in a:
    if(i not in b):
        b.append(i)
for i in b:
    print(i,"-",a.count(i))
---------------------------------------------------
4. ip:f46feLK9y56u#@&56hIjbn6KJhA
   op:
    lowervowel-
    uppervowel-
    lowerconsonant-
    upperconsonant-
    digits-
    specialcharacters-
a=""
uv,uc,lv,lc,d,s=0,0,0,0,0,0
for i in a:
    if(i.isupper()):
        if(i in 'AEIOU'):
            uv=uv+1
        else:
            uc=uc+1
    elif(i.islower()):
        if(i in 'aeiou'):
            lv=lv+1
        else:
            lc=lc+1
    elif(i.isdigit()):
        d=d+1
    elif(not i.isalnum()):
        s=s+1
print(uv,"-",uv)
print(uc,"-",uc)
print(lv,"-",lv)
print(lc,"-",lc)
--------------------------------------------
5. ip:placements
   op:consonants should be lower case
      vowels should be upper case

a="placements"
res=''
for i in a:
    if(i in 'aeiou'):
        res+=i.upper()
    else:
        res+=i
print(res)
--------------------------------------------
6.  ip:5 3.8 3 5.6 6 7"
    op:15
       9.4
       6
a=input()
a=a.split()
evensum,oddsum,digitsum=0,0,0
for i in a:
   if '.' in i:
       digitsum+=float(i)
   elif int(i)%2==0:
        evensum+=int(i)
   else:
        oddsum+=int(i)
print("Even sum:",evensum)
print("Odd sum:",oddsum)
print("Digit sum:",digitsum)  
-----------------------------------------------
7.numbers divisible by 7 between 300 t0 400
    ip:start range:300 t0 400
    for i in range(299,401):
       if i%7==0:
           print(i)
        
        (or) 
(300/7)-(400/7)
------------------------------------------------
_________Prime Number_________
8. ip:14
   op:17

n=int(input())
while(1):
    c=0
    for i in range(2,(n//2)+1):
        if(n%i==0):
            c=c+1
            break
    if(c==0):
        print(n)
        break
    else:
        n=n+1
------------------------------------------------
count of number of prime digits in a number
9.ip:7854
  op:2
  
n=int(input())
c=0
while(n):
    if(n%10 in [2,3,5,7]):
        c=c+1
    n=n//10
print(c)
------------------------------------------------
_________String Validation_____________
10.check whether the password is strong or not if not how
much count requires to make it strong password.
ip:asd123!@#
op:1

ip:123456789
op:3

ip:ab
op:6

ip:A1234B
op:2

ip:A1234a@4
op:-1

ip:1234567
op:3

ip:a123456
op:2

ip:abcdef127
op:2

n = input()
u,l,s,d=0,0,0,0
for i in n:
    if(i.isdigit()):
        d=1
    elif(i.islower()):
        l=1
    elif(i.isupper()):
        u=1
    else:
        s=1
m=4-(d+l+u+s)
if(len(n)+m)<8:
    print(len(n)-m)'''