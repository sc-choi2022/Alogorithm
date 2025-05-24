from heapq import heappush, heappop
import sys

N, H, T = map(int, sys.stdin.readline().split())

height = []
for _ in range(N):
    heappush(height, -(int(sys.stdin.readline())))

cnt = 0

for i in range(T):
    magic = -1*heappop(height)

    if magic == 1:
        heappush(height, -1)
    elif magic < H:
        heappush(height, -1*magic)
    else:
        heappush(height, -1*(magic//2))
        cnt += 1

result = -1*heappop(height)
if result >= H:
    print('NO')
    print(result)
else:
    print('YES')
    print(cnt)