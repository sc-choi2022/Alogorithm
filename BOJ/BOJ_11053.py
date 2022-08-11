# 수열의 크기 N
N = int(input())
# 수열 A
A = list(map(int, input().split()))
# i번째 위치까지 가장 긴 증가하는 부분 수열을 길이를 담을 리스트 dp
dp = [0] * N

for i in range(N):
    for j in range(i):
        # 증가하는 부분이고 이전 길이 중 큰 길이를 구하고
        if A[i] > A[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
        # 그 길이에 1을 증가
        number = A[i]
    dp[i] += 1
# 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력
print(max(dp))