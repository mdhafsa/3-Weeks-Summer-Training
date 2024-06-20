'''def solve_n_queens(n):
    def is_safe(board, row, col):
        
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        
        i, j = row, col
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1

        i, j = row, col
        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        return True

    def solve(board, row):
        if row >= n:
            solutions.append(["".join(row) for row in board])
            return
        
        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = 'Q'
                solve(board, row + 1)
                board[row][col] = '|'

    solutions = []
    board = [['|' for _ in range(n)] for _ in range(n)]
    solve(board, 0)
    return solutions

n =4
solutions = solve_n_queens(n)
for solution in solutions:
    for row in solution:
        print(row)
    print()'''
#----------------------------------------------------------------------

'''def queen(r):
    if(r==n):
        return
    if(r!=u):
        for c in range(n):
            if(check(r,c)):
                m[r][c]=1
                break
        return queen(r+1)
    else:
        return queen(r+1)
def check(i,j):
    if(i==u):
        return 0
    if(j==v):
        return 0
    r=i
    c=j
    for i in range(r+1):
        if(m[i][j]==1):
            return 0
    i=r
    while(i>=0 and j>=0):
        if(m[i][j]==1):
            return 0
        i=i-1
        j=j-1
    while(r>=0 and c<n):
        if(m[r][c]==1):
            return 0
        r=r-1
        c=c+1
    return 1
n=5
u=1
v=3
m=[]
for i in range(n):
    m.append([0]*n)
queen(0)
print(m)'''
#------------------------------------------------------------------

'''arr = [2, 5, 2, 3, 6, 7, 1, 0, 5, 7]
sunrise=0
max_mrng=0
for height in arr:
    if height>max_mrng:
        sunrise+=1
        max_mrng=height
sunset=0
max_evng=0
for height in reversed(arr):
    if height>max_evng:
        sunset+=1
        max_evng=height
print(sunrise)
print(sunset)'''
#-------------------------------------------------------------------
'''ip:[2,3,5,6]
op:11'''

#input:[2,3,5,6]
#output:11

'''def subset_sum(coins, target):
    dp = [False] * (target + 1)
    dp[0] = True
    
    for coin in coins:
        for j in range(target, coin - 1, -1):
            if dp[j - coin]:
                dp[j] = True
    
    return dp[target]

coins = [2, 3, 5, 6]
target = 12

if subset_sum(coins, target):
    print("yes")
else:
    print("no")'''

#--------------------------------------------------------------------
'''ip:tu5g1k1h7
   g5g3gd1h3
op:521863'''

'''a=input()
b=input()
c=set()
for i in a:
    if(i.isdigit()):
        c.add(i)
for i in b:
    if(i.isdigit()):
        c.add(i)
d=list(sorted(c,reverse=True))
if(int(d[-1])%2==0):
    print(''.join(d))
else:
    for i in range(len(c)-2,-1,-1):
        if(int(d[i])%2==0):
            d.append(d.pop(i))
            print(''.join(d))
            break
    else:
        print(-1)'''


'''ip:121
op:121
---------------------------------
ip:122
op:131
---------------------------------
ip:1234
op:1331
---------------------------------
ip:24
op:33
---------------------------------
ip:1112
op:1221
---------------------------------
ip:7654
op:7667
---------------------------------
ip:56472
op:56565
-----------------------------------------
ip:12412
op:12421'''
#-------------------------------------------------------------------------------------

'''ip:abdbsdabca
print longest palindromic substring if it is present print it else print -1
op:bdb'''

'''def longest_palindromic_substring(s):
    if not s:
        return -1

    def expand_around_center(s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    longest = ""
    for i in range(len(s)):
        # Odd-length palindromes
        odd_palindrome = expand_around_center(s, i, i)
        if len(odd_palindrome) > len(longest):
            longest = odd_palindrome

        # Even-length palindromes
        even_palindrome = expand_around_center(s, i, i + 1)
        if len(even_palindrome) > len(longest):
            longest = even_palindrome

    return longest if longest else -1

# Test the function with the given input
input_string = "abdbsdabca"
result = longest_palindromic_substring(input_string)
print(result)'''








        

            
            

   






    

    