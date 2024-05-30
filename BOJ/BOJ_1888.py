from collections import deque
import sys

# 곰팡이가 있는 위치를 저장하는 함수 place
def place():
    for i in range(M):
        for j in range(N):
            if wall[i][j]:
                mold[wall[i][j]].append((i, j))

# 덩어리를 확인하는 함수 check
def check():
    queue = deque([])
    visit = [[0]*N for _ in range(M)]
    # 덩어리의 개수 cnt
    cnt = 0
    for ci in range(M):
        for cj in range(N):
            if wall[ci][cj] and not visit[ci][cj]:
                queue.append((ci, cj))
                visit[ci][cj] = 1
                cnt += 1
                # 한 덩어리가 아닌 경우 return False
                if cnt > 1:
                    return False
                while queue:
                    si, sj = queue.popleft()

                    for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
                        ni, nj = si+di, sj+dj
                        if 0 <= ni < M and 0 <= nj < N and wall[ni][nj] and not visit[ni][nj]:
                            queue.append((ni, nj))
                            visit[ni][nj] = 1
    # 한 덩어리인 경우 return True
    return True

# 벽의 크기 M, N
M, N = map(int, sys.stdin.readline().split())
# 벽의 곰팡이를 저장하는 배열 wall
wall = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(M)]
# 곰팡이들의 숫자를 저장하는 배열 mold
mold = [[] for _ in range(6)]

answer = 0
while True:
    place()
    if check():
        break

    answer += 1
    for k in range(5, 0, -1):
        for _ in range(len(mold[k])):
            ci, cj = mold[k].pop()
            minI, maxI = max(0, ci-k), min(M, ci+k+1)
            minJ, maxJ = max(0, cj-k), min(N, cj+k+1)
            for ii in range(minI, maxI):
                for jj in range(minJ, maxJ):
                    if wall[ii][jj] < k:
                        wall[ii][jj] = k

# 곰팡이가 한 덩어리가 되기까지 걸리는 시간을 하루 단위로 출력
print(answer)