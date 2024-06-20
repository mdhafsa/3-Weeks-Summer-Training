#binary search not done in linked list because we have no indexing
#double linked list
class node:
    def __init__(self,x):
        self.data=x
        self.next=None
        self.prev=None

class dll:
    def __init__(self):
        self.head=None
        self.tail=None
        
    def addback(self,x):
        if self.head==None:
            self.head=node(x)
            self.tail=self.head
        else:
            t=node(x)
            self.tail.next=t
            t.prev=self.tail
            self.tail=self.tail.next
    
    def addfront(self,x):
        if(self.head==None):
            self.head=node(x)
            self.tail=self.head
        else:
            t=node(x)
            t.next=self.head
            self.head.prev=t
            self.head=t
    
    def linear_search(self, x):
        t = self.head
        t1=self.tail
        while (t!=t1 and t!=t1.next):
            if (t1.data==x or t.data == x):
                return 1
            t=t.next
            t1=t1.prev
        if(t.data==x):
            return 1
        else:
            return 0
    
    def find_len(self):
        t = self.head
        t1=self.tail
        while (t!=t1 and t!=t1.next):
            t=t.next
            t1=t1.prev
        if(t==t1):
            return "odd"
        else:
            return "even"
    
    def palin(self):
        t= self.head
        t1= self.tail
        while t!=t1 and t.prev!= t1:
            if t.data!= t1.data:
                return False
            t=t.next
            t1=t1.prev
        return True
    
    def half_rev(self):
        f=self.head
        s=self.head
        while(f!=None):
            f=f.next.next
            s=s.next
        t=self.head
        t1=s
        while(t1!=None):
            t.data,t1.data=t1.data,t.data
            t=t.next
            t1=t1.next
        
    def display(self):
        t=self.head
        while(t!=None):
            print(t.data,end="->")
            t=t.next
        print()
    '''def revlinks(self):
        p=None
        current=self.head
        n=current.next
        while(current.next.next!=None and n.next!=None):
            if(current==self.head):
                current.next=n.next
                n.next=current
                n.prev=current.prev
                current.prev=n
                self.head=n
                current,n=n,current
            else:
                current.next=n.next
                n.next=current
                n.prev=p
                current.prev=n
                p.next=n
                current,n=n,current
                p=n
                p=p.next.next
        current=current.next.next
        n=n.next.next'''
    
    def even_odd(self):
        t=self.head
        even_sum=0
        odd_sum=0
        while(t!=None):
            if(t.data%2==0):
                even_sum=even_sum+t.data
                t=t.next
            else:
                odd_sum=odd_sum+t.data
                t=t.next
        return abs(even_sum-odd_sum)
    
    def eos(self,t,es,os):
        if(t==None):
            return abs(es-os)
        if(t.data%2==0):
            es=es+t.data
        else:
            os=os+t.data
        return self.eos(t.next,es,os)
    def pr(self,t,c):
        if(t==None):
            return c
        def pnt(s,n):
            if(s>=(n//2)+1):
                return 1
            if(n%s==0):
                return 0
            return pnt(s+1,n)
        if(pnt(2,t.data)):
            c+=1
        return self.pr(t.next,c)

        
        
        
l1=dll()
l1.addback(20)
l1.addback(10)
l1.addback(121)
l1.addfront(10)
l1.addfront(121)
l1.addfront(2)
l1.display()
print(l1.linear_search(20))
print(l1.find_len())  
print(l1.palin())
l1.half_rev()
l1.display()
print(l1.even_odd())
print(l1.eos(l1.head,0,0))
print(l1.pr())
'''l1.revlinks()'''
l1.display()
