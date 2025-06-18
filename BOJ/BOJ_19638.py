from heapq import heappush, heappop
import sys

# 거인의 인구수 N, 센티의 키 H, 뿅망치의 횟수 제한 T
N, H, T = map(int, sys.stdin.readline().split())

# 거인의 키를 저장 height
height = []
for _ in range(N):
    heappush(height, -(int(sys.stdin.readline())))

# 뿅망치의 사용 횟수 cnt
cnt = 0

for i in range(T):
    magic = -1*heappop(height)

    if magic >= H:
        heappush(height, -1*(magic//2))
        cnt += 1
    else:
        heappush(height, -1*magic)

# 뿅망치의 최소 사용 횟수 혹은 키가 가장 큰 거인의 키
result = -1*heappop(height)

# 뿅망치 횟수를 사용 후 세티보다 키가 큰 거인이 있는 경우
if result >= H:
    print('NO')
    print(result)
# 모든 거인이 센티보다 키가 작도록 할 수 있는 경우
else:
    print('YES')
    print(cnt)