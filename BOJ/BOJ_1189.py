import sys

def dfs(ci, cj, cnt):
    global answer

    if cnt > K:
        return
    if (ci, cj) == (0, C-1) and cnt == K:
        answer += 1
        return
    for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
        ni, nj = ci + di, cj + dj

        if 0 <= ni < R and 0 <= nj < C and graph[ni][nj] != 'T' and not visit[ni][nj]:
            visit[ni][nj] = 1
            dfs(ni, nj, cnt+1)
            visit[ni][nj] = 0

# 맵의 크기 RxC, 거리의 길이 K
R, C, K = map(int, sys.stdin.readline().split())
# 맵의 내용을 저장하는 배열 graph
graph = [list(sys.stdin.readline().rstrip()) for _ in range(R)]
visit = [[0]*C for _ in range(R)]
visit[R-1][0] = 1
# 거리가 K인 가짓수 answer
answer = 0

dfs(R-1, 0, 1)
print(answer)