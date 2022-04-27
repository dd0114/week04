import sys
A = []









N = int(input())
path = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * (1<<N)]