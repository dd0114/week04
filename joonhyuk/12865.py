import sys

inp = sys.stdin.readline
outp = sys.stdout.write

n, m = list(map(int, inp().split()))
num = [[] for _ in range(n)]
for i in range(n):
    num[i] = list(map(int, inp().split()))

li = [[] for _ in range(n)]
weight = [[] for _ in range(n)]
maximum = 0
print(num)
print(li)
for i in range(n):
    for j in range(n):
        if i == j:
            if i == 0:
                li[i].append(0)
                weight[i].append(0)
            else:
                li[i].append(li[i - 1][j])
                weight[i].append(weight[i - 1][j])
            continue
        if i == 0:
            li[i].append(num[i][1] + num[j][1])
            weight[i].append(num[i][0] + num[j][0])
        else:
            li[i].append(num[i][1] + li[i - 1][j])
            weight[i].append(num[i][0] + weight[i - 1][j])
        if li[i][j] > maximum and weight[i][j] <= m:
            maximum = li[i][j]
print(li)
print(weight)
print(maximum)


