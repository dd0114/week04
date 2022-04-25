import sys
from collections import deque
import copy
n, k = map(int,sys.stdin.readline().split())


blist=[]

for _ in range(n):
    w,v = map(int,sys.stdin.readline().split())
    blist.append((w,v))

# check = [([0]*n)for _ in range(k+1)]
value = [0]*(k+1)

first = [0]*n
q = deque([[0,first]])

while q:
    pop = q.popleft()
    a = pop[0]
    b = pop[1]

    for i in range(n):
        n_w = a + blist[i][0]
        n_v = value[a] + blist[i][1]
        if b[i] == 0 and n_w <= k:
            if value[n_w] <= n_v:
                value[n_w] = n_v
            nb = copy.deepcopy(b)
            nb[i] = 1 
            q.append([n_w,nb])

print(value[k])
# for j in range(k+1):
#     for i in blist:
#         newv = dp[j-i]+dp[i]

#         if newv > dp[j]:
#             dp[j] = newv