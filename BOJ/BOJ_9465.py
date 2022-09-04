import sys

# 테스트 케이스 개수
T = int(sys.stdin.readline())

for _ in range(T):
    # 열의 개수 N
    N = int(sys.stdin.readline())
    # 스티커의 점수를 담은 배열 sticker
    sticker = [list(map(int, sys.stdin.readline().split())) for _ in range(2)]
    # (i,j)의 스티커를 포함하는 최대값을 (i,j)에 저장하는 배열 dp
    dp = [[0]*(N+1) for _ in range(2)]
    # 각 행의 sticker[0][0], sticker[1][0]에 첫번째 값을 저장
    dp[0][1], dp[1][1] = sticker[0][0], sticker[1][0]
    for i in range(2, N+1):
        # 각 위치의 값을 포함하는 최대값은 다른 행렬의 i-1열과 i-2열의 값 중 큰 값을 더한 값이다.
        dp[0][i] = sticker[0][i - 1] + max(dp[1][i - 1], dp[1][i - 2])
        dp[1][i] = sticker[1][i - 1] + max(dp[0][i - 1], dp[0][i - 2])
    # dp[0][N], dp[1][N]의 값 중 큰 값을 출력
    print(max(dp[0][N], dp[1][N]))