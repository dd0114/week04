import sys

n = int(input())

nlist = [0] * (n+2)

nlist[1] = 1

for i in range(n):
    nlist[i+2] = nlist[i+1]%15746 + nlist[i]%15746

print(nlist[n+1]%15746)