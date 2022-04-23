import sys
sys.setrecursionlimit(10*9)

t = int(input())

for _ in range(t):
    n = int(input())
    coin = list(map(int,sys.stdin.readline().split()))
    coin.sort(reverse=True)
    goal = int(input())     
    dp = [0]*(goal+1)
    for i in coin:
        dp[i] = 1

    for c in coin:
        for i in range(goal):
            if c +i <= goal :
                dp[c+i] += dp[i]
    print(dp[goal])