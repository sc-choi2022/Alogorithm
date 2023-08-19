import sys

# 테스트케이스의 수 T
T = int(sys.stdin.readline())

for _ in range(T):
    # 배열의 크기 N
    N = int(sys.stdin.readline())
    #
    dp = [0] * N
    numbers = list(map(int, sys.stdin.readline().split()))
    dp[0] = numbers[0]

    for i in range(1, N):
        dp[i] = max(numbers[i], dp[i-1] + numbers[i])
    # maximum subarray의 합을 줄로 구분하여 출력
    print(max(dp))