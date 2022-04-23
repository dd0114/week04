import sys


num = int(sys.stdin.readline())
llist = [0] * 1_000_001
llist[1] = 1
llist[2] = 2

for i in range(3, num+1):
    llist[i] = (llist[i-1] + llist[i-2])%15746

print(llist[num])




# 재귀로 풀면 	런타임 에러 (RecursionError) 뜸

# import sys

# llist = [0] * 1_000_001

# def fibo(x):
#     if x == 1:
#         return 1
#     if x == 2:
#         return 2
#     if llist[x] != 0:
#         return llist[x]
#     llist[x] = (fibo(x-1) + fibo(x-2))%15746
#     return llist[x]

# num = int(sys.stdin.readline())
# print(fibo(num))