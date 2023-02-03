import sys

# 자연수 N
N = int(sys.stdin.readline())
# 자연수 x의 제곱항의 최대값을 초기값으로 가지는 배열 dp
dp = [x for x in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, i):
        # j**2이 제곱항으로 가능한 수보다 큰 경우
        if j ** 2 > i:
            break
        # 기존 dp[i]인 i를 만드는 제곱항의 개수보다 dp[i - j**2] + 1이 작다면 dp[i] 갱신
        if dp[i] > dp[i - j**2] + 1:
            dp[i] = dp[i - j**2] + 1

# 제곱수 항의 최소 개수를 출력
print(dp[N])