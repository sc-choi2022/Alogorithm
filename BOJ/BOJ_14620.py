import sys

def dfs(cnt, cost):
    global answer
    if cnt == 3:
        answer = min(answer, cost)
        return
    for i in range(1, N-1):
        for j in range(1, N-1):
            if plant(i, j):
                visit[i][j] = 1
                for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
                    visit[i+di][j+dj] = 1
                    cost += flowers[i+di][j+dj]
                dfs(cnt+1, cost+flowers[i][j])
                for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
                    visit[i+di][j+dj] = 0
                    cost -= flowers[i+di][j+dj]
                visit[i][j] = 0

def plant(ci, cj):
    for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
        ni, nj = ci + di, cj + dj
        if 0 <= ni < N and 0 <= nj < N and not visit[ni][nj]:
            continue
        else:
            return False
    return True
# 화단의 한 변의 길이 N
N = int(sys.stdin.readline())
# 화단의 가격을 저장하는 배열 flowers
flowers = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# 꽃의 위치를 저장하는 배열 visit
visit = [[0]*N for _ in range(N)]

# 화단에 사용되는 꽃의 최소비용 answer
answer = 200000

dfs(0, 0)
# 꽃을 심기 위한 최소 비용을 출력
print(answer)