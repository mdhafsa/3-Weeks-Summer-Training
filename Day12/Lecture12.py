#bfs
'''def bfs(G,x):
        q.append(x)
        while(q):
            a=q.pop()
            if a not in v:
                v.append(a)
            for i in G[a]:
                if i not in v:
                    q.append(i)
        return v
G={5:[7,3],7:[5,4,3],4:[7,8,2],8:[3,4,2,10],3:[5,7,8,20],2:[4,8,15],10:[8,12],12:[10],15:[2],20:[3]}
q=[]
v=[]
print(bfs(G,5))'''
#----------------------------------------------------------------------------------
#dijikstras Algorithm
'''def bfs(x):
    d={4:999,1:9999,3:9999,5:9999,2:9999}
    d[x]=0
    vi=[]
    q=[x]
    while(q):
        m=9999
        for i in q:
            if(d[i]<m):
                m=d[i]
                x=i
        for i in g[x]:
            if (i[0] not in vi):
                q.append(i[0])
                if d[i[0]]>i[1]+d[x]:
                    d[i[0]]=i[1]+d[x]
        vi.append(x)
        q.remove(x)
    return d
               
g={4:[(1,5),(2,4),(3,3),(5,2)],1:[(2,2),(3,1),(4,5)],3:[(1,1),(4,3),(5,2)],5:[(3,2),(4,2)],2:[(1,2),(4,4)]}
print(bfs(4))'''
#---------------------------------------------------------------------------------------------------------------
'''ip:l1=[6,3,2,9,4,7]
   l2=[8,7,5,3,6,9]
op:l3=[13,11,9,15,9,7,5,11,11,9,7,13]

   
                
l1=[6,3,2,9,4,7]
l2=[8,7,5,3,6,9]
l3=[]
for i in l1:
    for j in l2:
        if i%2==0 and j%2!=0:
            l3.append(i+j)
print(l3)'''
#------------------------------------------------------------------------------------------------------------------

'''def match(l1,l2):
    def even_odd(l1,l2,i,j,res):
        if i>=len(l1):
            return res
        if j>=len(l2):
            return even_odd(l1,l2,i+1,0,res)
        if l1[i]%2==0 and l2[j]%2!=0:
            res.append((l1[i]+l2[j]))
        return even_odd(l1,l2,i,j+1,res)
    return even_odd(l1,l2,0,0,[])
            
    
l1=[6,3,2,9,4,7]
l2=[8,7,5,3,6,9]
res=match(l1,l2)
print(res)'''





   

    
              

    





