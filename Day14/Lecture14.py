
#####################Trapping Water###########################



#      |   |
#     ||   |
#  |  ||  ||
#  |  ||  ||
#  | |||  ||
# ||||||  ||
# ||||||| ||


# arr=[0,1,0,2,1,0,1,3,2,1,2,1]
# l=[0]*len(arr)
# r=[0]*len(arr)
# m=0
# for i in range(len(arr)):
#     if(arr[i]>m):
#         m=arr[i]
#     l[i]=m
# m1=0
# for i in range(len(arr)-1,-1,-1):
#     if(arr[i]>m1):
#         m1=arr[i]
#     r[i]=m1
# s=0
# for i in range(len(arr)):
#     s=s+abs(min(l[i],r[i])-arr[i])
# print(s)


###################### minimum coins possible to get the n value ##############
# def fun():
#     l1=[-1]*(n+1)
#     l1[0]=0
#     for i in l:
#         for j in range(1,n+1):
#             if(j>=i):
#                 if(l1[j-i]!=-1):
#                     if(l1[j]!=-1):
#                         l1[j]=min(l1[j],l1[j-i]+1)
#                     else:
#                         l1[j]=l1[j-i]+1
#     print(l1)
#     print(l1[-1])
# l=[1,3,4,5]
# n=17
# fun()



'''def fun(i,j,c):
    if(i<0 or i>=n or j>=m or j<0):#(i == k and j == l):
        return c
    if (i==n-1 and j==m-1):
        c = c+1
        return c
    vi.append((i,j))
    if((i-1,j) not in vi):
        c = fun(i-1,j,c)
    if((i+1,j) not in vi):
        c = fun(i+1,j,c)
    if((i,j-1) not in vi):
        c = fun(i,j-1,c)
    if((i,j+1) not in vi):
        c = fun(i,j+1,c)
    vi.pop()
    return c
n = int(input())
m = int(input())
vi=[]
print(fun(0,0,0))'''



