import sys

# N번째 피보나치 수열
N = int(sys.stdin.readline())

# 파사노 주기를 활용
# 피보나치 수를 나누는 값 M
M = 1000000
# 주기의 길이 P
P = M//10*15

# 피보나치 수열을 저장하는 배열 dp
dp = [0, 1] + [0] * (P-2)

for i in range(2, P):
    dp[i] = (dp[i-1]+dp[i-2])%M

# N번째 피보나치 수를 1,000,000으로 나눈 나머지를 출력
print(dp[N%P])