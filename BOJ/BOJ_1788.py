import sys

N = int(sys.stdin.readline())
if N < 0 and not abs(N) % 2:
    print(-1)
# N이 양수이거나 N이 음수이면서 절댓값이 홀수인 경우
elif N > 0 or (N < 0 and abs(N) % 2):
    print(1)
else:
    print(0)

N = abs(N)
dp = [0, 1] + [0] * (N-1)
for i in range(2, N+1):
    dp[i] = (dp[i-2] + dp[i-1])%1000000000
# F(N)의 절댓값 출력
print(dp[abs(N)])