from heapq import heapify, heappush, heappop
import sys

# 집의 수 N
N = int(sys.stdin.readline())
# 각각의 집 앞에 쌓여 있는 눈의 양 snow
snow = list(map(int, sys.stdin.readline().split()))
# 집 앞의 눈을 치우는 데 걸리는 분 answer
answer = 0
# 집이 한 채 인 경우
if N == 1:
    answer = snow[0]
else:
    heap = []
    for s in snow:
        heappush(heap, -s)

    while len(heap) > 1:
        C1 = -heappop(heap)
        C2 = -heappop(heap) if heap else 0

        answer += C2
        heappush(heap, C2-C1)
    # 치워야하는 눈이 남은 경우 더한다.
    answer += -heappop(heap) if heap else 0

# 모든 집 앞의 눈을 치우는 데 최소 몇 분이 걸리는지를 출력
# 24시간(1440분)이 넘게 걸릴 경우 -1을 출력
print(-1 if answer > 1440 else answer)