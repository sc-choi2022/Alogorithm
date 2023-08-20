import sys

# 테스트케이스의 수 T
T = int(sys.stdin.readline())

for _ in range(T):
    # 배열의 크기 N
    N = int(sys.stdin.readline())
    # maximum subarray의 합을 저장하는 배열 dp
    dp = [0] * N
    # 배열 X를 저장하는 배열 numbers
    numbers = list(map(int, sys.stdin.readline().split()))
    # dp[0]을 numbers[0]으로 초기화
    dp[0] = numbers[0]

    for i in range(1, N):
        dp[i] = max(numbers[i], dp[i-1] + numbers[i])
    # maximum subarray의 합을 줄로 구분하여 출력
    print(max(dp))