import sys

n = int(input())

hlist= [0]*(n+1)

for i in range(n):
    a ,b = map(int,sys.stdin.readline().split())
    hlist[i] = a
    hlist[i+1] = b

dp = [0]*(n+1)

if n > 1:
    dp[2] = hlist[0]*hlist[1]*hlist[2]

if n > 2:
    for i in range(3,n+1):
        first = dp[i-2] + hlist[i]*hlist[i-1]*hlist[i-2] + hlist[0]*hlist[i-2]*hlist[i]
        end = dp[i-1] + hlist[0]*hlist[i-1]*hlist[i]
        dp[i] = min(first,end) 

print(dp[n])