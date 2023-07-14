import sys

def fireball():
    return 

# 격자의 크기 N, 파이어볼의 개수 M, 이동 횟수 K
N, M, K = map(int, sys.stdin.readline().split())

for _ in range(M):
    # 파이어 볼의 위치 r, c, 질량 m, 속력 s, 방향 d
    r, c, m, s, d = map(int, sys.stdin.readline().split())

for _ in range(K):
    fireball()