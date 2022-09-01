import sys
import heapq

N = int(input())
arr = []

for _ in range(N):
    x = int(sys.stdin.readline())
    if x:
        heapq.heappush(arr, x)
    else:
        try:
            print(heapq.heappop(arr))
        except:
            print(0)