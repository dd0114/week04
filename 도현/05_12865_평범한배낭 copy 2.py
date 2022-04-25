import sys
from collections import deque
n, k = map(int,sys.stdin.readline().split())

blist=[0]

for _ in range(n):
    w,v = map(int,sys.stdin.readline().split())
    blist.append((w,v))

check = [([0]*(k+1))for _ in range(n+1)]


for i in range(1,n+1):
    for j in range(1,k+1):
        if j - blist[i][0] >= 0 :
            new_v = check[i-1][j - blist[i][0]] + blist[i][1]  
            if check[i-1][j] < new_v :
                check[i][j] = new_v

            else :
                check[i][j] = check[i-1][j]
        else :
            check[i][j] = check[i-1][j]
print(check[n][k])