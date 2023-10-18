from collections import deque
import sys

def location():
    # 빨간 구슬의 위치 (ri, rj), 파란 구슬의 위치 (bi, bj)
    ri, rj, bi, bj = -1, -1, -1, -1
    for li in range(N):
        for lj in range(M):
            if board[li][lj] == 'R':
                ri, rj = li, lj
            elif board[li][lj] == 'B':
                bi, bj = li, lj
    return (ri, rj, bi, bj)

def bfs():
    ri, rj, bi, bj = location()
    queue = deque([(ri, rj, bi, bj)])
    visit = [(ri, rj, bi, bj)]
    # 움직이는 횟수 cnt
    cnt = 0

    while queue:
        for _ in range(len(queue)):
            Ri, Rj, Bi, Bj = queue.popleft()
            # 10번 이하로 움직여서 빨간 구슬을 구멍을 통해 빼낼 수 없는 경우
            if cnt > 10:
                return -1
            # 빨간 구슬이 구멍을 나온 경우
            if board[Ri][Rj] == 'O':
                return cnt
            for di, dj in (-1, 0), (1, 0), (0, -1), (0, 1):
                nRi, nRj = Ri, Rj
                while True:
                    nRi += di
                    nRj += dj
                    if board[nRi][nRj] == '#':
                        nRi -= di
                        nRj -= dj
                        break
                    elif board[nRi][nRj] == 'O':
                        break
                nBi, nBj = Bi, Bj
                while True:
                    nBi += di
                    nBj += dj
                    if board[nBi][nBj] == '#':
                        nBi -= di
                        nBj -= dj
                        break
                    elif board[nBi][nBj] == 'O':
                        break
                if board[nBi][nBj] == 'O':
                    continue
                # 빨강 구슬과 파랑 구슬이 동일 위치에 존재하는 경우
                if (nRi, nRj) == (nBi, nBj):
                    # 더 많이 움직인 구슬을 이동
                    if abs(nRi-Ri) + abs(nRj-Rj) > abs(nBi-Bi) + abs(nBj-Bj):
                        nRi -= di
                        nRj -= dj
                    else:
                        nBi -= di
                        nBj -= dj
                if (nRi, nRj, nBi, nBj) not in visit:
                    queue.append((nRi, nRj, nBi, nBj))
                    visit.append((nRi, nRj, nBi, nBj))
        cnt += 1
    return -1

# 보드의 세로, 가로 크기 N, M
N, M = map(int, sys.stdin.readline().split())
# 보드의 상태를 저장하는 배열 board
board = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
# 최소 몇 번 만에 빨간 구슬을 구멍을 통해 빼낼 수 있는지 출력
print(bfs())