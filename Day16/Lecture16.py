'''ip:number of quries:7
1 school
1 world
1 word
1 scholar
2 word
2 wood
3 sch
op:
    True
    False
    True

ip:7
1 car
1 cap
2 ca
3 ca
1 can
3 ca
2 cap
op:False
   True
   True
   True
n=int(input())
l=[]
res=[]
for i in range(n):
    x,y=input().split(' ')
    l.append([x,y])
print(l)
for i in l:
    if i[0]=='1':
        res.append(i[1])
    if i[0]=='2':
        if i[1] in res:
            print("True")
        else:
            print("False")
    if i[0]=='3':
        found = False
        for i in res:
            if i[1] in i:
                found = True
                break
        if found:
            print("True")
        else:
            print("False")
print(res) '''

#---------------------------------------------------
'''ip:5
1 word
1 word
3 wo
4 word
2 word
op:1
  false'''

'''n=int(input())
l=[]
res=[]
for i in range(n):
    x,y=input().split(' ')
    l.append([x,y])
print(l)
for i in l:
    if i[0]=='1':
        res.append(i[1])
    if i[0]=='2':
        if i[1] in res:
            print("True")
        else:
            print("False")
    if i[0]=='3':
        c=0
        for i in res:
            if i[1] in i:
                c=c+1
                break
        print(c)
    if i[0]=='4':
         new_res = []
         for word in res:
             if word != i[1]:
                 new_res.append(word)
         res = new_res'''
#------------------------------------------------
#############################################TRIES########################################################
class node:
    def __init__(self):
        self.d={}
        self.flag=0
class tries:
    def __init__(self):
        self.root=node()
    def insert(self,str):
        t=self.root
        for i in str:
            if i not in t.d:
                t.d[i]=node()
            t=t.d[i]
        t.flag=1
    def search_word(self,str):
        t=self.root
        for i in str:
            if (i not in t.d):
                return False
            t=t.d[i]
        if(t.flag==1):
            return True
        else:
            return False
    def search_prefix(self,str):
        t=self.root
        for i in str:
            if (i not in t.d):
                return False
            t=t.d[i]
        return True
    def print_all_prefix(self,str):
        def fun(t,s):
            if(t.flag==1):
                print(s)
            for i in t.d:
                fun(t.d[i],s+i)
        t=self.root
        s=""
        for i in str:
            if (i in t.d):
                s=s+i
                t=t.d[i]
            else:
                return
        fun(t,s)
    def longest_prefix_string(self,str):
        
                               
t1=tries()



'''t1.insert("world")
t1.insert("word")
t1.insert("woo")
t1.insert("wo")'''
'''print(t1.search_word("wxyz"))
print(t1.search_word("world"))
print(t1.search_prefix("wox"))
print(t1.search_prefix("wor"))'''

'''n=int(input())
for i in range(n):
    a,s=input().split()
    if (a=="1"):
        t1.insert(s)
    if(a=="2"):
        print(t1.search_word(s))
    if(a=="3"):
        print(t1.search_prefix(s))
    if(a=='4'):
        t1.print_all_prefix(s)'''

