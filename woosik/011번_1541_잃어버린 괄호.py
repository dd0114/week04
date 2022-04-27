import sys

# split로 분리해서 + 나온 것들 더하고 - 나온 것들 더해서 뺀다.

strr = sys.stdin.readline().split('-')

llist = []

for i in strr:
    cnt = 0
    i = i.split('+')
    for j in i:
        cnt += int(j)
    llist.append(cnt)

n = llist[0]
for i in range(1, len(llist)):
    n -= llist[i]

print(n)