# 집의 수 N
N = int(input())

# N개의 줄에는 각 집을 빨강, 초록, 파랑으로 칠하는 비용을 담은 리스트 p
p = [list(map(int, input().split())) for _ in range(N)]
# i번째 집까지 칠하는 비용의 최솟값을 담을 리스트 dp
dp = [[0]*N for _ in range(N)]
# dp[0]은 p[0]로 저장
dp[0] = p[0]

for i in range(1, N):
    # 이전 집의 다른 두 색을 칠하는 비용 중 작은 값에 현재 위치 각 색을 칠하는 비용을 더해
    # R은 index 0, G은 index 1, B은 index 2에 저장
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + p[i][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + p[i][1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + p[i][2]
# dp[N-1]의 값 중 min값 출력
print(min(dp[N - 1][0], dp[N - 1][1], dp[N - 1][2]))