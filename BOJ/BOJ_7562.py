from collections import deque
import sys

# si, sj에서 i, j로 가는 최소 횟수를 구하는 함수 bfs
def bfs(si, sj):
    queue = deque([(si, sj)])

    while queue:
        ci, cj = queue.popleft()
        # 나이트의 이동가능한 모든 방향
        for di, dj in (-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1):
            ni, nj = ci + di, cj + dj

            if 0 <= ni < L and 0 <= nj < L and chess[ni][nj] == 0:
                chess[ni][nj] = chess[ci][cj] + 1
                queue.append((ni, nj))
                # 목적지 i, j에 도달한 경우 chess[ni][nj]의 값을 return
                if ni == i and nj == j:
                    return chess[ni][nj]

# 테스트 케이스 T
T = int(sys.stdin.readline())

for _ in range(T):
    # 체스판의 한변의 길이 L
    L = int(sys.stdin.readline())
    chess = [[0]*L for _ in range(L)]
    # 나이트가 현재 있는 칸 (si, sj)
    si, sj = map(int, sys.stdin.readline().split())
    # 나이트가 이동하려고 하는 칸 (i, j)
    i, j = map(int, sys.stdin.readline().split())
    # 이미 (i, j)에 도달한 경우 0 출력
    if si == i and sj == j:
        print(0)
    else:
        # 함수 bfs의 return 값을 출력
        print(bfs(si, sj))