import sys

first = input()
second = input()
first = '0'+first
second = '0'+second

check= [[0]*(len(second)) for _ in range(len(first))]

dot = []
result =0

for i in range(1,len(first)):
    for j in range(1,len(second)):
        if first[i] == second[j]:
            check[i][j] = check[i-1][j-1] +1

        else :
            check[i][j]=max(check[i][j-1],check[i-1][j])

print(check[-1][-1])

