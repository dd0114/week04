import sys
sys.setrecursionlimit(10*9)

t = int(input())

for _ in range(t):
    n = int(input())

    coin = list(map(int,sys.stdin.readline().split()))
    m = int(input())

    dp = [0]*(m+1)
    dp[0] = 1

    # i는 코인
    # j는 코스트

    for i in coin:
        for j in range(m):
            if j + i <= m:
                dp[j+i] += dp[j]
    
    print(dp[m])