import sys

# fibonacci함수에 인자로 입력할 N
N = int(sys.stdin.readline())
# fibonacci 함수가 호출된 횟수를 저장하는 배열 dp
dp = [1] * (N+1)

for i in range(2, N+1):
    dp[i] = (dp[i-1] + dp[i-2] + 1) % 1000000007

# fibonacci 함수가 호출된 횟수를 출력
print(dp[N])