import sys

def plus():
    return

def play():
    return

# 세로선의 개수 N, 가로선의 개수 M, 세로선마다 가로선을 놓을 수 있는 위치 개수 H
N, M, H = map(int, sys.stdin.readline().split())
lader = [[0]*N for _ in range(H)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    lader[a-1][b-1] = 1

answer = M+1

if answer > 3 or answer == M+1:
    print(-1)
else:
    print(answer)