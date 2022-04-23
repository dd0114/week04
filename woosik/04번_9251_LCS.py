import sys

strr1 = sys.stdin.readline().rstrip().upper()
strr2 = sys.stdin.readline().rstrip().upper()

len1 = len(strr1)
len2 = len(strr2)

llist = [[0] * (len2+1) for _ in range(len1+1)]

for i in range(1, len1+1):
    for j in range(1, len2+1):
        if strr1[i-1] == strr2[j-1]:
            llist[i][j] = llist[i-1][j-1] + 1
        else:
            llist[i][j] = max(llist[i][j-1], llist[i-1][j])
print(llist[-1][-1])