import sys
from collections import deque
import copy
n, k = map(int,sys.stdin.readline().split())


blist=[]

blist = []

for _ in range(n):
    w,v = map(int,sys.stdin.readline().split())
    blist.append((w,v))

check = [([0]*n)for _ in range(k+1)]
value = [0]*(k+1)

q = deque([0])

while q:
    a = q.popleft()
    for i in range(n):
        n_w = a + blist[i][0]
        n_v = value[a] + blist[i][1]
        if check[a][i] == 0 and n_w <= k:
        
            if value[n_w] < n_v:
                value[n_w] = n_v
            
            check[n_w] = copy.deepcopy(check[a])
            check[n_w][i] = 1
            q.append(n_w)

print(value[k])