import sys

num = int(sys.stdin.readline())
llist = list(map(int, sys.stdin.readline().split()))

dp = [1] * 1004

for i in range(num):
    for j in range(i):
        if llist[i] > llist[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))