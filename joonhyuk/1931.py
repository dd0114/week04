import sys

inp = sys.stdin.readline
outp = sys.stdout.write

n = int(inp())
mylist = []

for _ in range(n):
    mylist.append(list(map(int, inp().split())))

mylist.sort()
# print(mylist)
left = mylist[0][0]
right = mylist[0][1]
count = 1
for i in range(1, n):
    if left <= mylist[i][0] and right >= mylist[i][1]:
        # print('ck', left, right)
        if mylist[i][0] == mylist[i][1] and right == mylist[i][1]:
            count += 1
        left = mylist[i][0]
        right = mylist[i][1]
        
    elif right <= mylist[i][0] and right <= mylist[i][1]:
        left = mylist[i][0]
        right = mylist[i][1]
        count += 1
        # print('ck', left, right)
print(count)