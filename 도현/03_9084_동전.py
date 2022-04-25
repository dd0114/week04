import sys
sys.setrecursionlimit(10*9)

t = int(input())

for _ in range(t):
    n = int(input())
    coin = list(map(int,sys.stdin.readline().split()))
    coin.sort(reverse=True)
    goal = int(input())     
    count =0
    mock = []
    guide = [0]*n

    for i in range(n):
        mock.append(goal//coin[i]+1)
    
    while True:
        for i in n:
            guide[i]
