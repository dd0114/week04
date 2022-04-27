import sys

n, k = map(int,sys.stdin.readline().split())

coin = []

for _ in range(n):
    coin.append(int(sys.stdin.readline()))


count = 0

for i in reversed(range(n)):
   if k >= coin[i] and k >0 :
       count += k // coin[i]
       k = k %coin[i]

print(count)
