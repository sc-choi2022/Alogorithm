import sys

# 선을 그은 횟수 N
N = int(sys.stdin.readline())
# 두 점의 위치를 저장하는 배열 dots
dots = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
dots.sort(key=lambda x:(x[0],x[1]))