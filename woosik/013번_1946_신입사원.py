import sys

num = int(sys.stdin.readline())

for _ in range(num):
    _case = int(sys.stdin.readline())
    llist = []
    cnt = 1

    for _ in range(_case):
        llist.append(list(map(int, sys.stdin.readline().rstrip().split())))
    
    llist.sort(key = lambda x: x[0])
    temp = llist[0][1]

    for i in range(1, _case):
        if temp > llist[i][1]:
            cnt += 1
            temp = llist[i][1]

    
    print(cnt)
