import sys

t = int(input())

for i in range(t):
    n = int(input())

    junior = []
    for j in range(n):
        a,b = map(int,sys.stdin.readline().split())
        junior.append((a,b))

    junior.sort()

    count = 0
    cut = junior[0][1]

    for j in range(1,n):
        if junior[j][1] < cut:
            cut = junior[j][1]
            count +=1
    
    print(count+1)

