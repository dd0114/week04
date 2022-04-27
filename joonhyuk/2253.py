# #success
# import sys

# n, m = list(map(int, sys.stdin.readline().split()))
# cases = [-1] * (n + 1)
# jump = [-1] * (n + 1)
# stones = [1] * (n + 1)

# for i in range(m):
#     stones[int(sys.stdin.readline())] = 0

# def pongdang():
#     cases[0] = 0
#     cases[1] = 0
#     jump[0] = 0
#     jump[1] = 0
#     for i in range(1, n + 1):
#         # cnt = 0
#         if stones[i] == 0:
#             continue
#         for j in range(1, i):
#             # i - j = difference of two array
#             if stones[j] == 0:
#                 continue
#             print('*** check up i:', i, 'j:', j, cases[j])
#             if cases[j] <= i - j + 1 and cases[j] >= i - j - 1:
#             # if cases[j] <= i - j + 1 and cases[j] >= i - j - 1:
#                 # filtering not neccesary part and final index should be passed
#                 if cases[j] < n - i + 1 or i == n:
#                     print('****** picked up i:', i, 'j:', j, cases[j])
#                     # print(i, j, cases[j])
#                     # print(i, j, cases[j])
#                     cases[i] = i - j
#                     jump[i] = jump[j] + 1
#                     break
#                 # cnt += 1

# pongdang()
# print(jump[n])


# print(cases)
# print(jump)
            
            

# fail
# import sys

# n, m = list(map(int, sys.stdin.readline().split()))
# # cases = [-1] * (n + 1)
# cases = [[0 for _ in range(col + 1)]for col in range(n + 1)]
# jump = [[]for _ in range(n + 1)]
# stones = [1] * (n + 1)

# print(cases)
# for i in range(m):
#     stones[int(sys.stdin.readline())] = 0

# def pongdang():
#     cases[0].append(0)
#     jump[0].append(0)
#     for i in range(1, n + 1):
#         # cnt = 0
#         if stones[i] == 0:
#             continue
#         for j in range(1, i):
#             # i - j = difference of two array
#             if stones[j] == 0:
#                 continue
#             print(i, j, cases[j])
#             lenCase = len(cases) - 1
#             for k in cases[j]:
#                 if cases[k] <= i - j + 1 and cases[k] >= i - j - 1:
#                     cases[i].append(i - j)
#                     jump[i].append(jump[j][k] + 1)
#                     break
#                     # cnt += 1

# pongdang()
# # print(jump[n])
# print(cases)
# print(jump)

import sys

n, m = list(map(int, sys.stdin.readline().split()))
cases = [[0] for _ in range(n + 1)]
jump = [[0] for _ in range(n + 1)]
stones = [1] * (n + 1)

for i in range(m):
    stones[int(sys.stdin.readline())] = 0

def pongdang():
    cases[0] = 0
    cases[1] = 0
    jump[0] = 0
    jump[1] = 0
    for i in range(1, n + 1):
        # cnt = 0
        if stones[i] == 0:
            continue
        for j in range(1, i):
            # i - j = difference of two array
            if stones[j] == 0:
                continue
            print('*** check up i:', i, 'j:', j, cases[j])
            if cases[j] <= i - j + 1 and cases[j] >= i - j - 1:
            # if cases[j] <= i - j + 1 and cases[j] >= i - j - 1:
                # filtering not neccesary part and final index should be passed
                if cases[j] < n - i + 1 or i == n:
                    print('****** picked up i:', i, 'j:', j, cases[j])
                    # print(i, j, cases[j])
                    # print(i, j, cases[j])
                    cases[i].append(i - j)
                    jump[i].append(jump[j] + 1)
                    break
                # cnt += 1

pongdang()
print(jump[n])


print(cases)
print(jump)