import sys

def dfs(now, cnt):
    global answer
    if now == B:
        answer = min(answer, cnt)
        return
    if cnt > answer:
        return
    for i in range(M):
        if visit[i] == 0:
            visit[i] = 1
            dfs(i, cnt + bus[now][i])
            visit[i] = 0

# 도시의 개수 N
N = int(sys.stdin.readline())
# 버스의 개수 M
M = int(sys.stdin.readline())

bus = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
# 출발 도시의 번호 A,도착지의 도시 번호 B
A, B = map(int, sys.stdin.readline().split())
# 출발 도시에서 도착 도시까지 가는데 드는 최소 비용 answer
answer = 1e+10
# 도시의 방문여부를 저장할 visit
visit = [0] * N
visit[A-1] = 1
dfs(A-1, 0)