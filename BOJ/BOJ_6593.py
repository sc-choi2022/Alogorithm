from collections import deque
import sys

# 시작 위치를 찾는 함수 find
def find():
    for fi in range(L):
        for fj in range(R):
            for fk in range(C):
                if building[fi][fj][fk] == 'S':
                    return (fi, fj, fk)

def bfs(si, sj, sk):
    # 방문 여부와 시간을 저장하는 배열 visit
    visit = [[[0]*C for _ in range(R)] for _ in range(L)]
    # 시작 위치를 표시
    visit[si][sj][sk] = 1

    queue = deque()
    queue.append((si, sj, sk))

    while queue:
        ci, cj, ck = queue.popleft()

        for di, dj, dk in (0, 0, 1), (0, 1, 0), (1, 0, 0), (0, 0, -1), (0, -1, 0), (-1, 0, 0):
            ni, nj, nk = ci + di, cj + dj, ck + dk
            # 범위 안에 있고 방문하지 않은 경우
            if 0 <= ni < L and 0 <= nj < R and 0 <= nk < C and not visit[ni][nj][nk]:
                # 비어있는 경우
                if building[ni][nj][nk] == '.':
                    queue.append((ni, nj, nk))
                    visit[ni][nj][nk] = visit[ci][cj][ck] + 1
                # 출구에 도착한 경우
                if building[ni][nj][nk] == 'E':
                    return visit[ci][cj][ck]
    # 출구에 도착하지 못한 경우
    return -1

while True:
    # 충수 L, 한 층의 행 R, 한 층의 열 C
    L, R, C = map(int, sys.stdin.readline().split())

    if L==0 and R==0 and C==0:
        break
    # 빌딩의 정보를 저장하는 배열 building
    building = [[] for _ in range(L)]
    for i in range(L):
        lst = [[] for _ in range(R)]
        for j in range(R):
            lst[j] = list(sys.stdin.readline().rstrip())
        # 층을 구분하는 빈 줄
        blank = sys.stdin.readline().rstrip()
        building[i] = lst
    # 시작위치 si, sj, sk
    si, sj, sk = find()
    # 탈출시간을 변수 time에 저장
    time = bfs(si, sj, sk)

    # 탈출 불가능한 경우
    if time == -1:
        print('Trapped!')
    # 탈출 가능한 경우
    else:
        print(f'Escaped in {time} minute(s).')