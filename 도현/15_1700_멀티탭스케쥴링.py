import sys
import heapq

n, k = map(int,sys.stdin.readline().split())

klist = list(map(int,sys.stdin.readline().split()))

stack = [[101]for _ in range(k+1)]
mtt = []
count = 0

for i in range(k):
    heapq.heappush(stack[klist[i]],i)

if k > n:
    s = 0
    while len(mtt) < n :
        now = klist[s] 
        for j in range(len(mtt)):
            if mtt[j][1] == now:
                heapq.heappop(stack[now])
                mtt[j] = (stack[now][0] * -1,mtt[j][1])
                heapq.heapify(mtt)
                s += 1
                break
        else:
            heapq.heappop(stack[now])
            heapq.heappush(mtt, (stack[now][0] * -1,now))
            s += 1


    for i in range(s,k):
        now = klist[i] 
        for j in range(n):
            if mtt[j][1] == now:        
                heapq.heappop(stack[now])
                mtt[j] = (stack[now][0] * -1,mtt[j][1])
                heapq.heapify(mtt)
                break

        else :
            heapq.heappop(mtt)
            heapq.heappop(stack[klist[i]])
            heapq.heappush(mtt,(stack[now][0]*-1,now))
            count +=1



print(count)
        