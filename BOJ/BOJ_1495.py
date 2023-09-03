import sys

# 곡의 개수 N, 시작 볼륨 S, 기준 값 M
N, S, M = map(int, sys.stdin.readline().split())
# 볼륨의 정보를 저장하는 volumes
volumes = list(map(int, sys.stdin.readline().split()))
# i+1번째 행에 i번째 곡에 가능한 볼륨의 여부를 저장하는 배열 dp
dp = [[0]*(M+1) for _ in range(N+1)]
# 시작 볼륨값을 저장
dp[0][S] = 1

for i in range(1, N+1):
    for j in range(M+1):
        # 이전 곡에서 가능한 볼륨인 경우
        if dp[i-1][j]:
            # 이번 곡에서 가능 여부 저장
            if 0 <= j-volumes[i-1] <= M:
                dp[i][j-volumes[i-1]] = 1
            if 0 <= j+volumes[i-1] <= M:
                dp[i][j+volumes[i-1]] = 1
# 가능한 마지막 곡의 볼륨 중 최댓값을 출력
for d in range(M,-1, -1):
    if dp[N][d]:
        print(d)
        break
# 마지막 곡을 연주할 수 없다면 -1을 출력
else:
    print(-1)