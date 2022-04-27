import sys


first = input()
second = input()

first = '0' + first
second = '0' + second

dp = [[0]*len(first) for _ in range(len(second))]

for i in range(1,len(second)):
    for j in range(1,len(first)):
        if first[j] == second[i]:
            save = dp[i-1][j-1]+1
            dp[i][j] = max(save, dp[i-1][j], dp[i][j-1])
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])


print (dp[len(second)-1][len(first)-1])
