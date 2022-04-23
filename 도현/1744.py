# 정렬 후 뒤에서 부터 묶는다

# 만약 a와 b 둘다 0이하라면 팝해서 묶는다 
# 둘다 0이하면

# 아니라면
# 뒤집는다
# 만약 ab가 둘다 1이상이면
# 뒤에서부터 팝한다

# 결과 추출

import sys
from collections import deque

n = int(input())

num = []

for i in range(n):
    num.append(int(input()))

num.sort()

num = deque(num)

result = 0
while len(num) >= 2 :
    if num[0]<=0 and num[1] <= 0 :
        a = num.popleft()
        b = num.popleft()
        result += a*b
    else :
        break

num.reverse()

while len(num) >= 2 :
    if num[0] >1 and num[1] > 1:
        a = num.popleft()
        b = num.popleft()
        result += a*b
    else: 
        break

result += sum(num)
print (result)
