a = [
    [1,  2, 4, 4, 5],
    [1,  3, 2, 1, 1],
    [2, 17, 1, 7, 1]
]

a = [
    [1,  2, -1, 4, 5],
    [1,  3,  2, 1, 1],
    [2, 17, -1, 7, 1]
]

n = len(a)
print("n = ")
print(n)
m = len(a[0])
print("m = ")
print(m)
# init dp
dp = [[0] * m for i in range(n)]

# init top leftmost corner
dp[0][0] = a[0][0]

# set the first row
for j in range(1,m):
    if a[0][j] != -1 and dp[0][j-1] != -1:
        dp[0][j] = dp[0][j-1] + a[0][j]
    else:
        dp[0][j] = -1

for i in dp:
    print(i)

# set the first column
for i in range(1,n):
    if a[i][0] != -1 and dp[i-1][0] != -1:
        dp[i][0] = dp[i-1][0] + a[i][0]
    else:
        dp[i][0] = -1

for i in dp:
    print(i)

# compute the rest
for i in range(1,n):
    for j in range(1,m):
        if a[i][j] != -1 and (dp[i-1][j] != -1 or dp[i][j-1] != -1):
            dp[i][j] = a[i][j] + max( dp[i-1][j], dp[i][j-1] )
        else:
            dp[i][j] = -1

i = n - 1
j = m - 1
res = []
while i > 0 and j > 0:
    if dp[i-1][j] < dp[i][j-1]:
        res.append('right')
        j -= 1
    else:
        res.append('down')
        i -= 1

while i > 0:
    res.append('down')
    i -= 1

while j > 0:
    res.append('right')
    j -= 1


res.reverse()

print(res)

for ddd in dp:
    print(ddd)
    
