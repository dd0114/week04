n = int(input())

flist = [0] * (n+1)

flist[1] = 1

for i in range(n-1):
    flist[i+2]= flist[i] + flist[i+1]

print(flist[n])

