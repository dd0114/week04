import sys

inp = sys.stdin.readline
outp = sys.stdout.write

n, m = list(map(int, inp().split()))
coins = []

for _ in range(n):
    coins.append(int(inp()))

count = 0
for i in range(n - 1, -1, -1):
    if coins[i] > m:
        continue
    
    count += m // coins[i]
    m = m % coins[i]

print(count)