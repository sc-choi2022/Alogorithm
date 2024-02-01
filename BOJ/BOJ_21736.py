from collections import deque
import sys

# 캠퍼스의 크기 N, M
N, M = map(int, sys.stdin.readline().split())
# 캠퍼스의 정보를 저장하는 배열 campus
campus = [[] for _ in range(N)]
# 도연이의 방문여부를 저장하는 배열 visit
visit = [[0]*M for _ in range(N)]
# 도연이의 시작 위치 si, sj
si, sj = 0, 0
# 도연이가 만날 수 있는 사람의 명수 cnt
cnt = 0
# 도연이의 위치의 학인 여부를 저장하는 변수 flag
flag = False

for i in range(N):
    campus[i] = list(sys.stdin.readline().rstrip())
    if flag:
        continue
    # 도연이의 위치가 있는 경우
    if 'I' in campus[i]:
        si, sj = i, campus[i].index('I')
        flag = True

queue = deque([(si, sj)])
visit[si][sj] = 1
while queue:
    ci, cj = queue.popleft()

    for di, dj in (1, 0), (0, 1), (-1, 0), (0, -1):
        ni, nj = ci + di, cj + dj

        if 0 <= ni < N and 0 <= nj < M and (campus[ni][nj] == 'P' or campus[ni][nj] == 'O') and not visit[ni][nj]:
            if campus[ni][nj] == 'P':
                cnt += 1
            queue.append((ni, nj))
            visit[ni][nj] = 1
# 도연이가 만날 수 있는 사람의 수를 출력한다. 단, 아무도 만나지 못한 경우 TT를 출력
print(cnt if cnt else 'TT')