import sys

n = int(input())

nlist = list(map(int,input().split()))
nlist = [0]+ nlist

dp = [[0]*(n+1) for _ in range(n+1)]

save = 0

# i번째 열을 채운다.
# j로 비교할 줄을 찾는다. i-1 부터 본인보다 작은 수가 나올때까지
for i in range(1,n+1):
    for j in range(i):
        if nlist[i] > nlist[j] :
            key = j

    for l in range(i+1, n+1):
        if nlist[i] < nlist[l]:
            save = dp[key][l-1] + 1
            gijon = max(dp[i][l-1],dp[key][l])
            if save > gijon:
                dp[i][l] = save
            else:
                dp[i][l] = gijon

        else :
            dp[i][l] = max(dp[i][l-1],dp[key][l])

if dp[n][n] ==0 :
    print(0)
else:
    print(dp[n][n]+1)