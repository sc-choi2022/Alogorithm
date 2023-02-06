from copy import deepcopy
import sys

# dfs를 활용
def dfs(i, j, color, greed):
    stack = [(i, j)]

    while stack:
        ci, cj = stack.pop()

        for di, dj in (1, 0), (0, 1), (-1, 0), (0, -1):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and greed[ni][nj] == color:
                stack.append((ni, nj))
                greed[ni][nj] = 0

# 그리드의 한 길이 N
N = int(sys.stdin.readline())
# 주어지는 그리드 grd
grd = [list(sys.stdin.readline().strip()) for _ in range(N)]
# 적록색맹의 시선의 그리드 clblind
clblind = deepcopy(grd)
# 적록색맹이 아닌 사람의 구역개수 ans1
ans1 = 0
# dfs로 ans1의 개수를 구한다.
for i in range(N):
    for j in range(N):
        now = grd[i][j]
        if now != 0:
            grd[i][j] = 0
            dfs(i, j, now, grd)
            ans1 += 1
# 적록색명의 구역개수 ans2
ans2 = 0
# clblind에 적록을 동일하게 재설정
for ii in range(N):
    for jj in range(N):
        if clblind[ii][jj] == 'G':
            clblind[ii][jj] = 'R'
# dfs로 ans2의 수를 구한다.
for iii in range(N):
    for jjj in range(N):
        now1 = clblind[iii][jjj]
        if now1 != 0:
            clblind[iii][jjj] = 0
            dfs(iii, jjj, now1, clblind)
            ans2 += 1
# 적록색약이 아닌 사람이 봤을 때의 구역의 개수와 적록색약인 사람이 봤을 때의 구역의 수를 공백으로 구분해 출력
print(ans1, ans2)

from collections import deque
import sys

def bfs(i, j, color, visit):
    queue = deque([(i, j)])

    while queue:
        ci, cj = queue.popleft()

        for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
            ni, nj = ci + di, cj + dj

            if 0 <= ni < N and 0 <= nj < N and visit[ni][nj] == 0 and grd[ni][nj] == color:
                queue.append((ni, nj))
                visit[ni][nj] = 1
                if grd[ni][nj] == 'R':
                    grd[ni][nj] = 'G'

# 그리드의 한길이 N
N = int(sys.stdin.readline())
# 그리드의 정보를 담을 grd
grd = [list(sys.stdin.readline()) for _ in range(N)]

# 적록색맹이 아닌 사람과 적록색맹인 사람의 확인 여부를 저장할 배열 visit1, visit2
visit1, visit2 = [[0] * N for _ in range(N)], [[0] * N for _ in range(N)]

# 적록색맹이 아닌 구역개수 ans, 적록색맹의 구역개수 ans1
ans1, ans2 = 0, 0
# bfs을 활용하여 ans의 개수를 구하고 grd에 적록의 구분이 없도록 반영
for i in range(N):
    for j in range(N):
        tmp = grd[i][j]
        if tmp == 'R':
            grd[i][j] = 'G'
        if visit1[i][j] == 0:
            bfs(i, j, tmp, visit1)
            ans1 += 1
# bfs을 활용하여 ans1의 개수를 구한다.
for ii in range(N):
    for jj in range(N):
        if visit2[ii][jj] == 0:
            bfs(ii, jj, grd[ii][jj], visit2)
            ans2 += 1
# 적록색약이 아닌 사람이 봤을 때의 구역의 개수와 적록색약인 사람이 봤을 때의 구역의 수를 공백으로 구분해 출력
print(ans1, ans2)