import sys

dp = [0] * 251
dp[0], dp[1] = 1, 1

for i in range(2, 251):
    dp[i] = dp[i-1] + 2*dp[i-2]

while True:
    try:
        # 정수 N
        N = int(sys.stdin.readline())
        # 2×N 직사각형을 채우는 방법의 수를 출력
        print(dp[N])
    except:
        break