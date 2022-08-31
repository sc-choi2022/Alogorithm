import heapq
import sys

# 연산의 개수 N
N = int(input())

arr = []

for _ in range(N):
    x = int(sys.stdin.readline())
    if x:
        heapq.heappush(arr, (-x, x))
    else:
        if len(arr) >= 1:
            print(heapq.heappop(arr)[1])
        else:
            print(0)