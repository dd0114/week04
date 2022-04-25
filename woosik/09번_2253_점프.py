N, M = map(int, input().split())
dp = [[float('inf')] * (int((2 * N)** 0.5) + 2) for _ in range(N + 1)] 
dp[1][0] = 0
stones = set([int(input()) for _ in range(M)])

for i in range(2, N + 1):
    if i in stones: continue
    for j in range(1, int((2 * i) ** 0.5) + 1):
        dp[i][j] = min(dp[i - j][j - 1], dp[i - j][j], dp[i - j][j + 1]) + 1

answer = min(dp[N])

print(answer if answer != float('inf') else -1)


'''
등차수열로 속도가 증가했을 때 k번째 돌에서 a만큼의 최대 속도를 가질 수 있고 
이는 k = a(a+1)/2 를 만족한다.

정리하면 a = sqrt(2 * k + (1/4)) - 1/2 이기 때문에 
i번 위치에서 int(sqrt(2 * i)) + 1까지 검사하면 가능한 모든 속도에서의 값을 조사할 수 있다.

'''