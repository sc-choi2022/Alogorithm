import sys

# 우리의 크기 2*N의 세로길이 N
N = int(sys.stdin.readline())

# 사자를 배치하는 경우의 수를 담을 배열 dp
dp = [1, 3] + [0]*(N - 1)

for i in range(2, N + 1):
    # 메모리 초과를 방지하기 위해 9901의 나머지 값을 dp에 저장
    dp[i] = (dp[i - 2] + 2 * dp[i - 1]) % 9901
# 사자를 배치하는 경우의 수를 9901로 나눈 나머지를 출력
print(dp[N])