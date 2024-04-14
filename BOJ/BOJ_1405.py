import sys

# 현재 위치 (si, sj), 이동 횟수 cnt, 단순한 여부 flag, 현재까지의 확률 num
def dfs(si, sj, cnt, num):
    global P

    # 이동횟수가 N회인 단순한 경우
    if cnt == N:
        P += num
        return

    for i in range(4):
        # 움직일 수 있는 방향인 경우
        if percentage[i]:
            di, dj = direction[i]
            ni, nj = si+di, sj+dj
            # 단순
            if not visit[ni][nj]:
                visit[ni][nj] = 1
                dfs(ni, nj, cnt+1, num*percentage[i])
                visit[ni][nj] = 0

# 행동을 취하는 횟수 N, (동,서,남,북)으로 이동할 확률을 담는 배열 percentage
N, *percentage = list(map(int, sys.stdin.readline().split()))
for j in range(4):
    percentage[j] /= 100
# 동서남북의 이동방향을 저장하는 딕셔너리 direction
direction = {0 : (0, 1), 1 : (0, -1), 2 : (1, 0), 3 : (-1, 0)}
# 단순한 경우의 수 P
P = 0
# 방문 여부를 저장하는 배열 visit
visit = [[0]*(2*N+1) for _ in range(2*N+1)]
visit[N][N] = 1

dfs(N, N, 0, 1)

# 로봇의 이동 경로가 단순할 확률을 출력
print(P)