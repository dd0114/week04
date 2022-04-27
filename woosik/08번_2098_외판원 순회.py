# 구글링 복붙 해설 이해



def tsp(cur, visited):
    if visited == (1 << num) -1 :
        if not graph[cur][0] == 0:
            return graph[cur][0]
        else:
            return 2147000000
    
    if not mask[cur][visited] == -1:
        return mask[cur][visited]
    
    cost = 2147000000
    for i in range(num):
        if not visited & (1 << i ) == 0:
            continue
        if graph[cur][i] == 0:
            continue

        cost = min(cost, tsp(i, visited | ( 1 << i)) + graph[cur][i])
    mask[cur][visited] = cost
    return cost


num = int(input())
graph = [list(map(int, input().split())) for _ in range(num)]
mask = [ [-1] * (1 << num) for _ in range(num) ]

print(tsp(0, 2))




# import sys
# n = int(sys.stdin.readline())
# graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# dp = [[0] * (1 << n - 1) for _ in range(n)]

# def solution(i, route):
    
#     if dp[i][route] != 0:
#         return dp[i][route]

#     if route == (1 << (n - 1)) - 1:
#         if graph[i][0]:
#             return graph[i][0]
#         else:
#             return 1e9

#     bound = 1e9
    
#     for j in range(1, n):
#         if not graph[i][j]:
#             continue
#         if route & (1 << j - 1):
#             continue
#         dist = graph[i][j] + solution(j, route | (1 << (j - 1)))
#         if bound > dist:
#             bound = dist
#     dp[i][route] = bound

#     return bound

# print(solution(0, 2))