import sys
A=[]
def go(now, trace):  
    if dp[now][trace]:
        return dp[now][trace]
    if trace == (1 << N)-1: # 모든 도시 방문 완료시,
        return path[now][0] if path[now][0] > 0 else MAX  #마지막 도시에서 출발도시로 가는 비용 리턴

    cost = MAX
    for i in range(1, N):
        if not trace & (1 << i) and path[now][i]: #비트 마스크를 이용한 방문확인 
            val = go(i, trace | (1 << i))         #recursion & 방문처리
            cost = min(cost, val+path[now][i])    #여러가지 case 중 최솟값 갱신

    dp[now][trace] = cost
    return dp[now][trace]
N = int(input())
path = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * (1 << N) for _ in range(N)]
MAX = sys.maxsize

print(go(0, 1))