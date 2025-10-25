import sys

# 버스의 개수 N, 터미널에 도착하는 시간 T
N, T = map(int, sys.stdin.readline().split())
result = []

for _ in range(N):
    S, I, C = map(int, sys.stdin.readline().split())
    time = [S+(I*c) for c in range(C)]
    if time[-1] < T:
        continue
    start, end, answer = 0, C-1, 0
    while start <= end:
        mid = (start+end)//2
        if time[mid] >= T:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1
    result.append(time[answer]-T)

if result:
    print(min(result))
else:
    print(-1)