import sys

# 암호 숫자를 담을 배열 N
N = [0] + list(map(int, sys.stdin.readline().rstrip()))
# 암호의 길이 L
L = len(N)
# 다이나믹 프로그래밍을 활용할 dp
dp = [0] * L

# 암호가 잘못된 경우
if N[1] == 0:
    print(0)
else:
    dp[0], dp[1] = 1, 1
    for i in range(2, L):
        # N[i]이 0이 아닌 경우
        if N[i]:
            dp[i] += dp[i-1]
        # 두자리수의 암호가 가능한 경우를 확인하기 위한 변수 tmp
        tmp = N[i-1] * 10 + N[i]
        # tmp이 암호화가능한 경우
        if 10 <= tmp and tmp <= 26:
            dp[i] += dp[i-2]
        dp[i] = dp[i] % 1000000
    # 나올 수 있는 해석의 가짓수 출력
    print(dp[L-1])