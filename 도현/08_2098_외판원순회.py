# 4
# 0 10 15 20
# 5 0 9 10
# 6 13 0 12
# 8 8 9 0

import sys
n = int(input())

links = []

for i in range(n):
    a = list(map(int,sys.stdin.readline().split()))
    links.append(a)

dp = [([]*n)for _ in range(n+1)]

dp[0] = links[0]

# i는 n번째 방문기준
# j는 n번째 방문해서 도착하는 지점
for i in range(1,n):
    for j in range(1,n):
        save = 10**9
        for k in range(1,n):
            if k != j :
                a = links[k][j]+dp[i-1][j]
                save = min(save, a)
        dp[i][j] = save

for i in range(1,n):
    dp[n][i] = dp[n-1][i] + links[i][0]

print(dp)
dp[n].pop(0)
print(min(dp[n])) 