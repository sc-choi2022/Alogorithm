import sys

def dfs(ci, cj, cnt):
    global answer
    answer = max(answer, cnt)

    for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
        ni, nj = ci + di, cj + dj
        if 0 <= ni < R and 0 <= nj < C and not visit[board[ni][nj]]:
            visit[board[ni][nj]] = 1
            dfs(ni, nj, cnt+1)
            visit[board[ni][nj]] = 0

# 세로의 길이 R, 가로의 길이 C
R, C = map(int, sys.stdin.readline().split())
# 보드에 적힌 알파벳을 0~25으로 변환하여 저장하는 배열 board
board = [list(map(lambda x:ord(x)-65, sys.stdin.readline().rstrip())) for _ in range(R)]
# 보드에 방문 여부를 저장하는 배열 visit
visit = [0]*26
# 말이 지날 수 있는 최대의 칸 수 answer
answer = 0

# 시작 위치의 정보를 alphabet에 반영
visit[board[0][0]] = 1, 1
dfs(0, 0, 1)

# 말이 지날 수 있는 최대의 칸 수를 출력
print(answer)