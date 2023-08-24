import sys

# 대나무 숲의 크기 N
N = int(sys.stdin.readline())
# 대나무 숲의 정보를 저장하는 배열 bamboo
bamboo = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# 판다가 이동할 수 있는 칸의 최대 수 answer
answer = 0

# dp + dfs
