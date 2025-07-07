from heapq import heappush, heappop
import sys

def test():
    global prefer
    for b in beer:
        if len(like) < N:
            heappush(like, b)
            prefer += b[0]
            if len(like) == N:
                if prefer >= M:
                    return b[1]
                else:
                    prefer -= heappop(like)[0]
    return -1

# 축제가 열리는 기간 N, 선호도의 합 M, 마실 수 있는 맥주 종류의 수 K
N, M, K = map(int, sys.stdin.readline().split())
beer = [tuple(map(int, sys.stdin.readline().split())) for _ in range(K)]
beer.sort(key=lambda x:x[1])

like = []

# 선호도의 합 prefer
prefer = 0

# 최솟값을 출력
# 조건을 만족시킬 수 없으면 -1 출력
print(test())