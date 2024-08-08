import sys

# 대포알의 개수 N
N = int(sys.stdin.readline())
# 대포알을 이루는 삼각형 여부를 저장하는 배열 balls
balls = []
B = 0
m = 1
# 대포알의 개수로 만들 수 있는 사면체의 최솟값을 저장하는 배열 dp
dp = [N+1] * (N+1)

while True:
    B += (m * (m+1))//2
    if B > N:
        break
    balls.append(B)
    dp[B] = 1
    m += 1

for i in range(1, N+1):
    for ball in balls:
        if ball > i:
            break
        dp[i] = min(dp[i], dp[i-ball]+1)
# 만들 수 있는 사면체 개수의 최솟값을 출력
print(dp[N])