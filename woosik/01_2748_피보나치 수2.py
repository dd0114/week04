import sys

llist = [0] * 100

def fibo(x):
    if x == 0:
        return 0
    if x == 1 or x == 2:
        return 1
    if llist[x] != 0:
        return llist[x]
    llist[x] = fibo(x-1) + fibo(x-2)
    return llist[x]

num = int(sys.stdin.readline())
print(fibo(num))