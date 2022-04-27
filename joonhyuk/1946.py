import sys

inp = sys.stdin.readline
outp = sys.stdout.write

n = int(inp())

for _ in range(n):
    m = int(inp())
    mylist = []
    for _ in range(m):
        mylist.append(list(map(int, inp().split())))
    mylist.sort()
    # print(mylist)   
    maxval = 0
    operand = mylist[0][1]
    count = 1
    operand = mylist[0][1]
    for i in range(1, m):
        if operand > mylist[i][1]:
            count += 1
            operand = mylist[i][1]
    print(count)

# import sys

# T = int(input())

# for _ in range(T):
#     count = 0
#     applicant_number = int(input())
#     d = sorted([tuple(map(int, sys.stdin.readline().split(' '))) for i in range(applicant_number)])

#     m = d[0][1]

#     for i in range(applicant_number):
#         if i == 0:
#             count += 1
#         else:
#             if m > d[i][1]:
#                 count += 1
#                 m = d[i][1]
#     print(count)