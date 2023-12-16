import sys

# 이닝 수 N
N = int(sys.stdin.readline())
# 얻을 수 있는 최대 점수 score
score = 0
# 이닝의 점수를 저장하는 배열 innings
innings = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]