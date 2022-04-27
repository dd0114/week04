import sys

# 그리디 기본 문제


n, k = map(int, sys.stdin.readline().split())
coins = []
cnt = 0

for _ in range(n):
    coins.append(int(sys.stdin.readline().rstrip()))

coins.sort(reverse=True)

for coin in coins:
    cnt += k // coin
    k = k % coin

print(cnt)