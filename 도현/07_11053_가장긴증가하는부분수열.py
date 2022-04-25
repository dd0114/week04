import sys

n = int(input())

nlist = list(map(int,input().split()))

dp = [[0]*n for _ in range(n)]

save = 0

for i in range(n):
    if nlist[0] < nlist[i]:
        save = 1

    if save == 1: 
        dp[0][i] = 1

# i번째 열을 채운다.
# j로 비교할 줄을 찾는다. i-1 부터 본인보다 작은 수가 나올때까지
for i in range(1,n):
    key = n
    # for 문 뒤에서 부터 엏게 돌리는지
    for j in range(i):
        if nlist[i] > nlist[j] :
            key = j

    if key == n :
        save = 0
        for k in range(n):
            if save == 0:                 
                if k > i :
                    save = 1
                    dp[i][k] = 1
            if save == 1:
                dp[i][k] = 1

        continue

    save = 0

    for l in range(n):
        if save == 0:
            if i < l:
                save = dp[key][l] + 1
                if save > dp[i][l-1] and save>dp[i-1][l]:
                    dp[i][l] = save
                else:
                    dp[i][l] = max(dp[i][l-1],dp[i-1],[l])
                    save = 0

        else :
            dp[i][l] = save

print(dp[n-1][n-1])