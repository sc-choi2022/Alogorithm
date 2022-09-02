from heapq import heappush, heappop
import sys

# 연산의 개수 N
N = int(sys.stdin.readline())
# 배열 heap
heap = []

for _ in range(N):
    # 정수 x
    x = int(sys.stdin.readline())
    # x가 0이 아니라면
    if x:
        heappush(heap, (abs(x), x))
    else:
        # 배열 heap이 비어있지 않다면
        if heap:
            # x을 출력
            print(heappop(heap)[1])
        else:
            # 0을 출력
            print(0)