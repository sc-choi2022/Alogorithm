from heapq import heappush, heappop
import sys

# 아이들과 거점지르 ㄹ방문한 횟수 N
N = int(sys.stdin.readline())
# 선물을 저장하는 배열 presents
presents = []
for _ in range(N):
    # 거점지 0 혹은 숫자 A와 선물의 가치를 담는 배열 tmp
    A, *tmp = list(map(int, sys.stdin.readline().split()))

    # 거점지인 경우
    if not A:
        # 선물을 가지고 있는 경우
        if presents:
            print(-heappop(presents))
        # 선물이 없는 경우
        else:
            print(-1)
    # 선물을 충전하는 경우
    else:
        for i in range(A):
            heappush(presents, -tmp[i])