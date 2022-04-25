import sys

n, k=map(int,input().split())
llist=[list(map(int, input().split())) for _ in range(n)]
dp=[[0]*(k+1) for _ in range(n+1)]

for i in range(1,n+1):
  for j in range(1, k+1):
    if j<llist[i-1][0]:
      dp[i][j]=dp[i-1][j]
    else:
      dp[i][j]=max(dp[i-1][j],dp[i-1][j-llist[i-1][0]]+llist[i-1][1])

print(dp[-1][-1])


"""
물건의 총 갯수 : N = 4
배낭의 최대 무게 : K = 7
물건의 무게와 물건의 가치 :  W, V
위의 정보가 주어졌을 때, 물건의 인덱스가 행이고
구분이 열인 matrix를 만든다. matrix의 값으로는 무게가 j 이하인 것
중에서 i 번째 물건까지 고려했을 때 최대의 가치를 갖는
물건의 가치 V 를 적는다. 
최대의 가치인지를 판별하는 식은 아래와 같다.


D[i][j] = 
if j < W[i]
    D[i-1][j]
if j>=W[i]
    max(D[i-1][j], D[i-1][j-W[i]]+V[i])


https://kils-log-of-develop.tistory.com/247
이 블로그에서 이 식은 외우라고 한다.
"""