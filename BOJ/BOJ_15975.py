import sys

# 점의 개수 N
N = int(sys.stdin.readline())

# 점의 정보를 저장하는 배열 dots
dots = [int(sys.stdin.readline()) for _ in range(N)]
dots.sort()