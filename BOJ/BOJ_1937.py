import sys
sys.setrecursionlimit(10**6)

def dfs(ci, cj):
    tmp = 1
    for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
        ni, nj = ci + di, cj + dj
        if 0 <= ni < N and 0 <= nj < N and bamboo[ci][cj] < bamboo[ni][nj]:
            if dp[ni][nj] != -1:
                tmp = max(tmp, dp[ni][nj] + 1)
            else:
                tmp = max(tmp, dfs(ni, nj) + 1)
    dp[ci][cj] = tmp
    return dp[ci][cj]

# 대나무 숲의 크기 N
N = int(sys.stdin.readline())
# 대나무 숲의 정보를 저장하는 배열 bamboo
bamboo = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [[-1]*N for _ in range(N)]
# 판다가 이동할 수 있는 칸의 최대 수 answer
answer = 0

for i in range(N):
    for j in range(N):
        answer = max(answer, dfs(i, j))
# 판다가 이동할 수 있는 칸의 수의 최댓값을 출력
print(answer)