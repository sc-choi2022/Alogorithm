# 수열의 크기 N
N = int(input())
# 수열 A
A = list(map(int, input().split()))
# A[i]을 포함하는 가장 긴 증가하는 부분 수열을 길이를 각 index에 담을 리스트 dp
dp = [0] * N

for i in range(N):
    for j in range(i):
        # 증가하는 부분이고 이전 길이 중 큰 길이를 구하고
        if A[i] > A[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    # i번째는 반드시 포함하므로 dp[i] 1 증가
    dp[i] += 1
# 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력
print(max(dp))