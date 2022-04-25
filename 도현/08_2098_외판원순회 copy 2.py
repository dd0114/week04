# 4
# 0 10 15 20
# 5 0 9 10
# 6 13 0 12
# 8 8 9 0

import sys
import copy
n = int(input())

links = []

for i in range(n):
    a = list(map(int,sys.stdin.readline().split()))
    links.append(a)

dp = [[[0]*(n+1)for _ in range(n)]for _ in range(n)]

# 0은 벨류, 1~n-1은 방문체크

for i in range(n):
    dp[0][i][i] = 1

# i는 n번째 방문기준
# j는 n번째 방문해서 도착하는 지점
for i in range(1,n):
    for j in range(n):
        save = 10**9
        # i 번째에 k점(j를 제외한점)에서 j점으로 오는 값중에 최솟값을 찾음
        for k in range(n):            
            if k!=j and dp[i-1][k][j] == 0 and dp[i-1][k][n] != 10**9:
                if save > dp[i-1][k][n]+links[k][j]:
                    save = dp[i-1][k][n]+links[k][j]
                    savedot = k

        dp[i][j] = copy.deepcopy(dp[i-1][savedot])
        dp[i][j][n] = save
        dp[i][j][j] = i+1


# for i in range(n):
#     if dp[n-2][i][n] != 10**9:
#         for j in range(n):
#             if dp[n-2][i][j] == 0:
                
#         # a = dp[n-2][i][n] + 

total = []

print(dp)