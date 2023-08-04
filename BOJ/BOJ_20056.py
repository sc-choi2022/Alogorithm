import sys

def fireball():
    global graph
    tmp = [[[] for _ in range(N)] for _ in range(N)]

    # 모든 파이어볼이 자신의 방야 d로 속력 s만큼 이동한다.
    for fi in range(N):
        for fj in range(N):
            if graph[fi][fj]:
                for g in graph[fi][fj]:
                    m, s, d = g
                    di, dj = direction[d]
                    ni, nj = (fi + s*di)%N, (fj + s*dj)%N
                    tmp[ni][nj].append((m, s, d))
    # 이동이 모두 끝난 뒤, 2개 이상의 파이어볼이 있는 칸에서는 다음과 같은 일이 일어난다.
    for si in range(N):
        for sj in range(N):
            if len(tmp[si][sj]) > 1:
                # 파이얼볼의 개수 cnt, 질량 합 mass, 속력 합 speed, 파이어볼의 종류 check, 동일 여부 flag
                cnt, mass, speed, check, flag = 0, 0, 0, -1, 1
                while tmp[si][sj]:
                    tmp_m, tmp_s, tmp_d = tmp[si][sj].pop()
                    cnt += 1
                    mass += tmp_m
                    speed += tmp_s
                    if check == -1:
                        check = tmp_d%2
                    elif check != tmp_d%2:
                        flag = 0

                if mass//5:
                    if flag:
                        directs = [0, 2, 4, 6]
                    else:
                        directs = [1, 3, 5, 7]
                    for direct in directs:
                        tmp[si][sj].append((mass//5, speed//cnt, direct))
    graph = tmp

# 격자의 크기 N, 파이어볼의 개수 M, 이동 횟수 K
N, M, K = map(int, sys.stdin.readline().split())
graph = [[[] for _ in range(N)] for _ in range(N)]
direction = {0:(-1, 0), 1:(-1, 1), 2:(0, 1), 3:(1, 1), 4:(1, 0), 5:(1, -1), 6:(0, -1), 7:(-1, -1)}
answer = 0

for _ in range(M):
    # 파이어 볼의 위치 r, c, 질량 m, 속력 s, 방향 d
    r, c, m, s, d = map(int, sys.stdin.readline().split())
    graph[r-1][c-1].append((m, s, d))

for _ in range(K):
    fireball()

for ai in range(N):
    for aj in range(N):
        if graph[ai][aj]:
            for a in graph[ai][aj]:
                answer += a[0]
# 마법사 상어가 이동을 K번 명령한 후, 남아있는 파이어볼 질량의 합을 출력
print(answer)