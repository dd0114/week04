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

dp = [[([0]*n)for _ in range(n)]for _ in range(n+1)]

# 0은 벨류, 1~n-1은 방문체크

for i in range(1,n):
    value = links[0][i]
    dp[0][i][0] = value
    dp[0][i][i] = 1


# i는 n번째 방문기준
# j는 n번째 방문해서 도착하는 지점
for i in range(1,n-2):
    for j in range(1,n):
        save = 10**9
        savedot = 0
        # i 번째에 k점(j를 제외한점)에서 j점으로 오는 값중에 최솟값을 찾음
        for k in range(1,n):            
            if k!=j and dp[i-1][k][j] == 0:
                if save > dp[i-1][k][0]+links[k][j]:
                    save = dp[i-1][k][0]+links[k][j]
                    savedot = k

        dp[i][j] = copy.deepcopy(dp[i-1][savedot])
        dp[i][j][0] = save
        dp[i][j][savedot] = 1


print(dp)
dp[n].pop(0)
print(min(dp[n])) 