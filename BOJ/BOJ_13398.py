import sys

# 수열에 포함된 정수의 개수 N
N = int(sys.stdin.readline())
# 수열을 저장하는 배열 A
A = list(map(int, sys.stdin.readline().split()))

if N == 1:
    print(A[0])
else:
    # 수열의 누적합을 저장하는 배열 dp
    # 원소를 제거하지 않은 경우 dp
    # 특정 원소를 제거한 경우 ddp
    dp = [0] * N
    ddp = [0] * N
    dp[0] = A[0]

    # 구할 수 있는 가장 큰 합 answer
    answer = -1001
    for i in range(1, N):
        dp[i] = max(dp[i-1] + A[i], A[i])
        ddp[i] = max(dp[i-1], ddp[i-1] + A[i])

        answer = max(answer, dp[i], ddp[i])
    # 연속된 수의 합 중 가장 큰 합을 출력
    print(answer)