import sys

inp = sys.stdin.readline
outp = sys.stdout.write

tilelist = [set(''), set('1'), set('00', '11')]
n = int(inp())

# def tile(n):
#     if n == 1:
#         return tilelist[1]
#     elif n == 2:
#         return tilelist[2]

#     li = n // 2 + 1
#     for i in range(1, li):
#         print(tile(i))
#         for j in tile(i):
#             if j != '\n':
#                 print(tile(n-i))
#                 for k in tile(n - i):
#                     if k != '\n':
#                         print(tilelist[1])
#                         tilelist[i].add((j+k))
# 
# tile(n)
tilelist[2].add(2)
print(tilelist[2])