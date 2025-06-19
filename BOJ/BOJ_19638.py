from heapq import heappush, heappop
import sys

# 센티를 제외한 거인 나라의 인구수 N, 센티의 키 H, 마법의 뿅망치 횟수 제한 T
N, H, T = map(int, sys.stdin.readline().split())

# 키를 저장하는 배열 heights
heights = []

for _ in range(N):
    heappush(heights, -int(sys.stdin.readline()))

# 마법의 뿅망치 사용 횟수 cnt
cnt = 0

for _ in range(T):
    # 거인 중 가장 큰 거인의 키 magic
    magic = -1*heappop(heights)

    if magic == 1:
        heappush(heights, -1)
    elif magic >= H:
        heappush(heights, -1*(magic//2))
        cnt += 1
    else:
        heappush(heights, -1*magic)

# 뿅망치 사용 후 가장 큰 거인의 키 giants
giants = -1*heappop(heights)

# 뿅망치 횟수를 사용 후 세티보다 키가 큰 거인이 있는 경우
if giants >= H:
    print('NO')
    print(giants)
# 모든 거인이 센티보다 키가 작도록 할 수 있는 경우
else:
    print('YES')
    print(cnt)