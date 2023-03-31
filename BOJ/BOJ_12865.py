import sys

# 물건의 수 N, 한도 무게 K
N, K = map(int, sys.stdin.readline().split())
# 물건의 무게와 가치를 담을 배열 things
things = [(0,0)] + [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
things.sort()
# 다이나믹 프로그래밍을 위한 배열 dp
dp = [[0]*(K+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        weight, value = things[i]
        # i번째 물건의 무게가 기준 무게 j보다 큰 경우
        # i-1번째 물건의 j 한도 무게까지의 최대 가치를 저장
        if weight > j:
            dp[i][j] = dp[i-1][j]
        # i번째 물건을 담을 수 있는 경우
        # 넣을 수 있는 최대 가치를 저장
        else:
            dp[i][j] = max(value + dp[i-1][j-weight], dp[i-1][j])

# N개의 물건 중 배낭에 넣을 수 있는 물건들의 가치합의 최댓값을 출력
print(dp[N][K])