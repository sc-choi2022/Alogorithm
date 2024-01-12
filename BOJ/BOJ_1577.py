import sys

# 길이 공사중인지 확인하는 함수 check
def check(current, x1, y1, x2, y2):
    if current == [x1, y1, x2, y2] or current == [x2, y2, x1, y1]:
        return True
    else:
        return False

# 도로의 가로 크기 N, 세로 크기 M
N, M = map(int, sys.stdin.readline().split())
# 공사중인 도로의 개수 K
K = int(sys.stdin.readline())
# 공사정보를 저장하는 배열 roads
roads = [list(map(int, sys.stdin.readline().split())) for _ in range(K)]
# [i][j]위치까지 최단거리로 가는 경우의 수를 저장하는 배열 dp
dp = [[0]*(N+1) for _ in range(M+1)]
# 세준이의 집에서 출발하는 방법 1가지를 저장
dp[0][0] = 1

for i in range(M+1):
    for j in range(N+1):
        # 시작점이 아닌 곳
        # 가로방향으로 움직이는 경우
        if j:
            for a, b, c, d in roads:
                if check([i, j-1, i, j], b, a, d, c):
                    break
            else:
                dp[i][j] += dp[i][j-1]
        # 세로방향으로 움직이는 경우
        if i:
            for a, b, c, d in roads:
                if check([i-1, j, i, j], b, a, d, c):
                    break
            else:
                dp[i][j] += dp[i-1][j]
# (0, 0)에서 (N, M)까지 가는 경우의 수를 출력
print(dp[M][N])