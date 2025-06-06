import sys

def find_start(target):
    start, end = 0, N-1
    while start <= end:
        mid = (start+end)//2
        if line[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return start

def find_end(target):
    start, end = 0, N-1
    while start <= end:
        mid = (start + end) // 2
        if line[mid] <= target:
            start = mid + 1
        else:
            end = mid - 1
    return start

# 점의 개수 N, 선분의 개수 M
N, M = map(int, sys.stdin.readline().split())
# 점의 좌표를 저장하는 배열 dots
dots = sorted(list(map(int, sys.stdin.readline().split())))
# 선분의 시작, 끝 점을 저장하는 배열 lines
lines = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

for line in lines:
    start, end = line
    start_idx = find_start()
    end_idx = find_end()