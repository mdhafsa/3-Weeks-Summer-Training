#single linked list
#adding the elements at back and front in the linked list
#adding the even elements in the linked list
#linear search in the linked list
#middle node in the linked list
#even or odd linkedlist
#count of the nodes in the linked list
#pairs in the linked list
#sorting the linked list using bubble sort

class node:
    def __init__(self,u):
        self.data=u
        self.nxt=None
class sll:
    def __init__(self):
        self.head=None
    def display(self):
        t=self.head
        while(t!=None):
            print(t.data,end="->")
            t=t.nxt
        print()
    def addfront(self,x):
        t=node(x)
        t.nxt=self.head
        self.head=t   
    def addback(self,x):
        t=self.head
        while(t.nxt!=None):
            t=t.nxt
        t.nxt=node(x)
    def addeven(self):
        s=0
        t=self.head
        while(t!=None):
            if(t.data%2==0):
                s=s+t.data
                t=t.nxt
        print(s)
    def linearsearch(self,x):
        t=self.head
        while(t!=None):
            if(t.data==x):
                print("found")
                break
            else:
                t=t.nxt
                print("not found")
                break
    def middlenode(self):
        fast=self.head
        slow=self.head
        while(fast!=None and fast.nxt!=None):
            slow=slow.nxt
            fast=fast.nxt.nxt
        print(slow.data)
            
    def lenlinked(self):
        fast=self.head
        slow=self.head
        while(fast!=None and fast.nxt!=None):
            slow=slow.nxt
            fast=fast.nxt.nxt
        if (fast==None):
            print("even")
        else:
            print("odd")
    def count(self):
        t=self.head
        c=1
        m=0
        while(t.nxt!=None):
            if((t.nxt.data-t.data)==1):
                c=c+1
            else:
                if(c>m):
                    m=c
                c=1
            t=t.nxt
        if(c>m):
            m=c      
        print(m)
    def pairs(self):
        x=[]
        T=self.head
        while(T.nxt!=None):
            t=T.nxt
            while(t!=None):
                x.append((T.data,t.data))
                t=t.nxt
            T=T.nxt
        print(x)
    def bubblesort(self):
        c=0
        T=self.head
        p=None
        while(T.nxt!=p):
            f=0
            t=self.head
            while(t.nxt!=p):
                if(t.data>t.nxt.data):
                    f=1
                    t.data,t.nxt.data=t.nxt.data,t.data
                t=t.nxt
                c=c+1
            if(f==0):
                break
            p=t
            T=T.nxt
        return c
    
                
            
l1=sll()
l2=sll()
l3=sll()
l1.head=node(10)
l1.addback(20)
l2.head=node(100)
l2.addback(200)
l1.addeven()
l1.linearsearch(10)
l1.addfront(30)
l1.display()
l2.display()
l1.middlenode()
l1.lenlinked()
l1.count()
l1.pairs()
l3.head=node(10)
l3.addback(6)
l3.addback(18)
l3.addback(1)
l3.display()
l3.bubblesort()
l3.display()