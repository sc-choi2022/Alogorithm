import sys

# 단원의 개수 N, 공부할 수 있는 총 시간 T
N, T = map(int, sys.stdin.readline().split())
# 예상 공부 시간 K, 문제의 배점 S을 저장하는 배열 study
study = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [0] * N