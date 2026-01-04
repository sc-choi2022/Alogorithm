from copy import deepcopy
import sys

def find():
    global K
    add = set()
    for fi in range(1, N):
        for fj in range(1, M):
            if board[fi][fj] == '*':
                pre = set()
                L = 1
                for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                    ni, nj = fi+L*di, fj+L*dj
                    # 십자가가 겹쳐지는 경우 표시 필요
                    if 0 <= ni < N and 0 <= nj < M and board[ni][nj] == '*':
                        pre.add((ni, nj))
                        visit[ni][nj] += 1
                    else:
                        if add:
                            K += 1
                        break
                    add.union(pre)
                    L += 1
    for pi, pj in add:
        visit[pi][pj] = 1

def check():
    for ci in range(N):
        for cj in range(M):
            if board[ci][cj] != visit[ci][cj]:
                return False
    return True


# 격자판의 크기 N, M
N, M = map(int, sys.stdin.readline().split())
# 격자판의 상태 board
board = [sys.stdin.readline().rstrip() for _ in range(N)]
tmp = deepcopy(board)
visit = [[0]*N for _ in range(M)]

# 필요한 십자가의 수 K
K = 0

find()

if check():
    print(K)
    for v in visit:
        print(*v)
else:
    print(-1)