import sys

n, k = map(int,sys.stdin.readline().split())

coin = []

for _ in range(n):
    coin.append(int(sys.stdin.readline()))


count = 0
kcount = 0

for i in range(n-1,-1,-1):
    while k > 0 and k >= coin[i]:
        k = k - coin[i]
        count += 1
print(count)
