import sys

# 테스트 케이스 개수 T
T = int(sys.stdin.readline())

# 1, 2, 3의 합으로 나타내는 방법의 수를 저장하는 배열 dp
dp = [[0, 0, 0] for _ in range(100001)]
# dp[1], dp[2], dp[3]의 값을 초기화
dp[1], dp[2], dp[3] = [1, 0, 0], [0, 1, 0], [1, 1, 1]

for i in range(4, 100001):
    dp[i] = [(dp[i - 1][1] + dp[i - 1][2]) % 1000000009, (dp[i - 2][0] + dp[i - 2][2]) % 1000000009, (dp[i - 3][0] + dp[i - 3][1]) % 1000000009]
for _ in range(T):
    # 정수 N
    N = int(sys.stdin.readline())
    # N을 1, 2, 3의 합으로 나타내는 방법의 수를 1,000,000,009로 나눈 나머지를 출력
    print(sum(dp[N])%1000000009)