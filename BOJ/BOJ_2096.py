import sys

# 줄의 개수 N
N = int(sys.stdin.readline())

# 이전 줄의 값의 최댓값 max_dp, 최솟값 min_dp
max_dp, min_dp = [0] * 3, [0] * 3
# 현재 줄의 값의 최댓값 max_tmp, 최솟값 min_tmp
max_tmp, min_tmp = [0] * 3, [0] * 3

for _ in range(N):
    a, b, c = map(int, sys.stdin.readline().split())

    for i in range(3):
        if i == 0:
            max_tmp[i] = a + max(max_dp[i], max_dp[i+1])
            min_tmp[i] = a + min(min_dp[i], min_dp[i+1])
        elif i == 1:
            max_tmp[i] = b + max(max_dp[i-1], max_dp[i], max_dp[i+1])
            min_tmp[i] = b + min(min_dp[i-1], min_dp[i], min_dp[i+1])
        else:
            max_tmp[i] = c + max(max_dp[i-1], max_dp[i])
            min_tmp[i] = c + min(min_dp[i-1], min_dp[i])

    for j in range(3):
        max_dp[j] = max_tmp[j]
        min_dp[j] = min_tmp[j]

# 얻을 수 있는 최대 점수와 최소 점수를 띄어서 출력
print(max(max_dp), min(min_dp))