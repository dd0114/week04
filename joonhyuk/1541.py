import sys

inp = sys.stdin.readline
outp = sys.stdout.write

instr = inp()
mylist = []
temp = ''

for chr in instr:
    if chr == '+' or chr == '-' or chr == '\n':
        mylist.append(int(temp))
        mylist.append(chr)
        temp = ''
    else:    
        temp += chr
# print(mylist)
out = 0
flag = 0
temp = 0
for i in range(len(mylist) - 2, -1, -1):   
    if mylist[i] == '-':
        out -= temp
        temp = 0
    elif mylist[i] == '+':
        continue
    else:
        temp += mylist[i]

print(out + temp)
