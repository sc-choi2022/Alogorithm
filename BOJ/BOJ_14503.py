import sys

# 방의 크기 N, M
N, M = map(int, sys.stdin.readline().split())
# 로봇 청소기가 있는 칸의 좌표 R, C, 바라보는 방향 D
R, C, D = map(int, sys.stdin.readline().split())
# 장소의 상태를 저장하는 배열 place
# 0: 청소가 되지 않은 칸, 1: 벽이 있는 것
place = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# 청소여부를 저장하는 배열 visit
visit = [[0]*M in range(M)]