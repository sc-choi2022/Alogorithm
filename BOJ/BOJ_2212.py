import sys

# 센서의 개수 N
N = int(sys.stdin.readline())
# 집중국의 개수 K
K = int(sys.stdin.readline())
# N개의 센서를 담는 배열 censors
censors = sorted(list(map(int, sys.stdin.readline().split())))

# 집중국의 수신 가능 영역의 길이 answer
answer = 0
# 집중국의 개수가 센서의 수보다 작은 경우
if K < N:
    gaps = [0]*(N-1)
    for i in range(1, N):
        gaps[i-1] = censors[i] - censors[i-1]
    gaps.sort()
    print(sum(gaps[:N-K]))
# 집중국의 개수가 센서의 수보다 큰 경우
else:
    print(0)