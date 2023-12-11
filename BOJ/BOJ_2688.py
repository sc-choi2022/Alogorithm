import sys

# 테스트 케이스 개수 T
T = int(sys.stdin.readline())
# 행을 숫자의 자리수로 열을 숫자의 시작수로 하는 숫자의 개수를 저장하는 배열 dp
dp = [[0] * 10 for _ in range(1001)]
dp[1] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
dp[2] = [i for i in range(10, 0, -1)]

for _ in range(T):
    # N자리 수의 개수 N
    N = int(sys.stdin.readline())
    # N자리 수의 개수가 이미 구해진 경우 sum(dp[N-1]) 출력
    if sum(dp[N]):
        print(sum(dp[N]))
        continue
    # N자리 수의 개수를 구해야하는 경우
    for j in range(2, N+1):
        if sum(dp[j]):
            continue
        dp[j][0] = sum(dp[j-1])
        for k in range(1, 10):
            dp[j][k] = dp[j][k-1] - dp[j-1][k-1]
    # N자리 수의 개수를 출력
    print(sum(dp[N]))