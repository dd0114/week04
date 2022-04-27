import sys
import copy

inp = sys.stdin.readline
outp = sys.stdout.write

n, m = list(map(int, inp().split()))
multi = list(map(int, inp().split()))
originmulti = [multi[0]]

for idx in range(1, m):
    if len(originmulti) == n:
        i = idx
        break
    if multi[idx] not in originmulti:
        originmulti.append(multi[idx])

cnt = 0

# print('i', i, ptr)
while i < m:
    if multi[i] in originmulti:
        i += 1
        continue
    ptr = i + 1
    templist = []
    while ptr < m and len(templist) + 1 < n:
        if multi[ptr] in originmulti and multi[ptr] not in templist:
            templist.append(multi[ptr])
        ptr += 1
    # print(i,templist)

    for idx in range(n):
        if originmulti[idx] not in templist:
            # print('ck', originmulti[idx], multi[idx])
            originmulti[idx] = multi[i]
            # print('ck', originmulti[idx], multi[idx])
            cnt += 1
            break
    # print(originmulti)
    i += 1
    

print(cnt)

# Fail
# import sys
# import copy

# inp = sys.stdin.readline
# outp = sys.stdout.write

# n, m = list(map(int, inp().split()))
# multi = list(map(int, inp().split()))
# originmulti = [multi[0]]
# for idx in range(1, m):
#     if len(originmulti) == n:
#         break
#     if multi[idx] not in originmulti:
#         originmulti.append(multi[idx])

# all = 0
# i = n
# ptr = i + n - 1
# # print('i', i, ptr)
# while i < m:
#     if m - i < n:
#         ptr = m - 1
#     tempmulti = []
#     count = 0
#     while count < n:
#         if i >= m:
#             break
#         if multi[i] not in tempmulti:
#             if not tempmulti and multi[i] in originmulti:
#                 i += 1
#                 continue
#             tempmulti.append(multi[i])
#             count += 1
#         i += 1
#     print(originmulti)
#     print(tempmulti)
#     difcount = 0
#     for j in range(count):
#         if tempmulti[j] not in originmulti:
#             difcount += 1
#     for j in range(count):
#         if tempmulti[j] not in originmulti:
#             originmulti = copy.deepcopy(tempmulti)
#             all += difcount
#             break
#     print('ck all:', all)
# print(all)



