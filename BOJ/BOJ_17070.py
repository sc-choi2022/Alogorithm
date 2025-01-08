# dfs
import sys

def move(si, sj, number):
    global answer

    if (si, sj) == (N-1, N-1):
        answer += 1
        return

    # 가로 파이프인 경우
    if number == 0:
        # 가로 파이프
        if sj+1 < N and not house[si][sj+1]:
            move(si, sj+1, 0)
        # 대각선 파이프
        if si+1 < N and sj+1 < N and not house[si+1][sj] and not house[si][sj+1] and not house[si+1][sj+1]:
            move(si+1, sj+1, 1)
    # 대각선 파이프인 경우
    elif number == 1:
        # 가로 파이프
        if sj+1 < N and not house[si][sj+1]:
            move(si, sj+1, 0)
        # 대각선 파이프
        if si+1 < N and sj+1 < N and not house[si+1][sj] and not house[si][sj+1] and not house[si+1][sj+1]:
            move(si+1, sj+1, 1)
        # 세로 파이프
        if si+1 < N and not house[si+1][sj]:
            move(si+1, sj, 2)
    # 세로 파이프인 경우
    else:
        # 대각선 파이프
        if si+1 < N and sj+1 < N and not house[si+1][sj] and not house[si][sj+1] and not house[si+1][sj+1]:
            move(si+1, sj+1, 1)
        # 세로 파이프
        if si+1 < N and not house[si+1][sj]:
            move(si+1, sj, 2)

# 집의 크기 N
N = int(sys.stdin.readline())
# 집의 상태를 저장하는 배열 house
house = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 가능한 이동횟수를 저장하는 변수 answer
answer = 0

move(0, 1, 0)
# 파이프의 한쪽 끝을 (N, N)으로 이동시키는 방법의 수 출력
print(answer)

# dp
import sys

# 집의 크기 N
N = int(sys.stdin.readline())
# 집의 상태를 저장하는 배열 house
house = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(3)]
dp[0][0][1] = 1

for h in range(2, N):
    if not house[0][h]:
        dp[0][0][h] = dp[0][0][h-1]

for i in range(1, N):
    for j in range(1, N):
        # 대각선 파이프를 추가
        if not house[i][j] and not house[i-1][j] and not house[i][j-1]:
            dp[1][i][j] = dp[0][i-1][j-1] + dp[1][i-1][j-1] + dp[2][i-1][j-1]
        # 가로 세로 파이프를 추가
        if not house[i][j]:
            dp[0][i][j] = dp[0][i][j-1] + dp[1][i][j-1]
            dp[2][i][j] = dp[2][i-1][j] + dp[1][i-1][j]

# 파이프의 한쪽 끝을 (N, N)으로 이동시키는 방법의 수 출력
print(dp[0][N-1][N-1]+dp[1][N-1][N-1]+dp[2][N-1][N-1])