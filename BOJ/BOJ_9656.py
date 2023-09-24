# dp
from collections import deque
import sys

# 돌의 개수 N
N = int(sys.stdin.readline())
# 가져간 돌의 주인을 저장할 배열 dp 0: 창영(CY), 1:상근(SK)
dp = [-1] * (N+1)

queue = deque([])

if N < 3:
    dp[1] = 0
    queue.append(1)
else:
    dp[1], dp[3] = 0, 0
    queue.append(1)
    queue.append(3)

while queue:
    current = queue.popleft()

    for next in current+1, current+3:
        if 0 <= next <= N and dp[next] == -1:
            if dp[current]:
                dp[next] = 0
                queue.append(next)
            else:
                dp[next] = 1
                queue.append(next)

if dp[N]:
    print('SK')
else:
    print('CY')

# 규칙
import sys
print('SK' if int(sys.stdin.readline()) % 2 == 0 else 'CY')

# dp
# 돌의 개수 N
N = int(sys.stdin.readline())
# 가져간 돌의 주인을 저장할 배열 dp 0: 창영(CY), 1:상근(SK)
dp = [0] * 1001
dp[1], dp[2], dp[3] = 'CY', 'SK', 'CY'

for i in range(4, N+1):
    for stone in (1, 3):
        if dp[i-stone] == 'CY':
            dp[i] = 'SK'
            break
        dp[i] = 'CY'
# 상근이가 게임을 이기면 SK를, 창영이가 게임을 이기면 CY을 출력
print(dp[N])