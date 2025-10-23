import sys

# 버스의 개수 N, 터미널에 도착하는 시간 T
N, T = map(int, sys.stdin.readline().split())

for _ in range(N):
    S, I, C = map(int, sys.stdin.readline().split())
    time = [S+(I*C) for c in range(C)]
    if time[-1] < T:
        continue
    start, end = 0, C-1
    while start <= end:
        mid = (start+end)//2
        if time[mid] >= T:
            answer = mid
            end = mid - 1