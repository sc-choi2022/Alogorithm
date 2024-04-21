import sys

# 정수의 개수 N
N = int(sys.stdin.readline())
# 정수를 저장하는 배열 numbers
numbers = list(map(int, sys.stdin.readline().split()))
# 최대 사용 횟수 K
K = int(sys.stdin.readline())
# 최대로 만들 수 있는 정수 M
M = numbers[-1] * K
# 최대로 만들 수 있는 수까지 필요한 사용횟수를 저장하는 배열 dp
dp = [50001] * (M + 1)
dp[0] = 0

for i in range(M):
    for number in numbers:
        if number + i <= M:
            dp[number+i] = min(dp[number+i], dp[i]+1)

for j in range(1, M+1):
    if dp[j] > K:
        # 홀수가 이긴 경우
        if not j%2:
            print(f'holsoon win at {j}')
        # 짝수가 이긴 경우
        else:
            print(f'jjaksoon win at {j}')
        break