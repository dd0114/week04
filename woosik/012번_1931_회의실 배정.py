import sys

num = int(sys.stdin.readline())

llist = []

for i in range(num):
    llist.append(list(map(int, sys.stdin.readline().rstrip().split())))


# 밑 sort 가 우선순위를 갖는다. 우식 sort 로 명명.
llist.sort(key = lambda x : x[0])
llist.sort(key = lambda x : x[1])

meeting_time = 0
cnt = 0

for i, j in llist:
    if i >= meeting_time:
        cnt += 1
        meeting_time = j

print(cnt)