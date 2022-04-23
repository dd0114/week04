import sys

_T = int(sys.stdin.readline())

for _ in range(_T):
    _N1 = int(sys.stdin.readline())
    coins = list(map(int, sys.stdin.readline().split()))
    m = int(sys.stdin.readline())

    llist = [0] * (m+1)
    llist[0] = 1

    for coin in coins:
        for i in range(m+1):                    # 여기부터
            if i >= coin:
                llist[i] += llist[i- coin]      # 여기까지
    print(llist[m])


# 점화식 DP[i] = DP[i-k] + DP[i]
# I 금액을 K금액의 동전으로 만드는 경우
