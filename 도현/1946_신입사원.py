import sys

t = int(input())

for i in range(t):
    n = int(input())

    junior = []
    junior2 = []
    for j in range(n):
        a,b = map(int,sys.stdin.readline().split())
        junior.append((a,b))
        junior2.append((a,b))

    junior.sort(reverse=True)
    junior2.sort(reverse=True, key= lambda x:(x[1]))

    count = 0

    for j in range(n):
        dot = 0
        if junior[j][0] > junior[j][1]:
            for k in range(junior[j][1],n):
                if junior[j][0] > junior2[k][0]:
                    dot = 1
                    break


        else : 
            for k in range(j+1,n):
                if junior[j][1] > junior[k][1]:
                    dot = 1
                    break
        
        if dot== 0:
            count +=1 
    
    print(count)

