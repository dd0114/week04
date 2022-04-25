n = int(input())

flist = [0]*(n+1)

flist[1]= 1


def fibo2(a):
    if a ==0 :
        return 0
    if a == 1 or a==2:
        return 1
    
    elif flist[a] :
        return flist[a]
    
    flist[a] = fibo2(a-1) +fibo2(a-2)
    return fibo2(a)

print(fibo2(n))

