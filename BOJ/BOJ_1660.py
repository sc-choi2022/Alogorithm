import sys

# 대포알의 개수 N
N = int(sys.stdin.readline())
# 대포알을 이루는 삼각형 여부를 저장하는 배열 balls
balls = [0] * (N+1)
B = 0
m = 1

while True:
    B += (m * (m+1))//2
    if B > N:
        break
    balls[B] = 1
    m += 1

MAX = sys.maxsize
dp = [MAX] * (N+1)

for i in range(1, N+1):
    for j in range(1, N+1):
        if balls[j] == 1:
            if j >= i:
                if j == i:
                    dp[i] = 1
                break
            dp[i] = min(dp[i], dp[i-j]+1)
print(dp[N])