import sys

# 좌석의 개수 N
N = int(sys.stdin.readline())
# VIP 회원 명수 M
M = int(sys.stdin.readline())
VIPS = [int(sys.stdin.readline()) for _ in range(M)]
dp = [1, 1, 2] + [0]*(N-2)

for i in range(3, N+1):
    dp[i] = dp[i-1] + dp[i-2]

answer = 1
if M:
    tmp = 0
    for VIP in VIPS:
        # VIP의 위치까지의 경우의 수를 answer에 곱하고 VIP의 위치를 tmp에 저장
        answer *= dp[VIP - tmp - 1]
        tmp = VIP
    # 마지막 VIP 위치 이후 좌석의 개수에 따른 경우의 수를 곱한다.
    answer *= dp[N-tmp]
else:
    answer = dp[N]
# 주어진 조건을 만족하면서 사람들이 좌석에 앉을 수 있는 방법의 가짓수를 출력
print(answer)