import sys

# 궁수를 배치
def location():
    return

# 행의 개수 N, 열의 수 M, 궁수의 공격 거리 제한 D
N, M, D = map(int, sys.stdin.readline().split())
# 격자판의 상태를 저장하는 배열 graph
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]