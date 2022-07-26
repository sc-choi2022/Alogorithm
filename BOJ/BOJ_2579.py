import sys

N = int(sys.stdin.readline())
# stairs, dp 리스트를 [0]*300으로 초기화
stairs, dp = [0]*300, [0]*300
for i in range(N):
    stairs[i] = int(sys.stdin.readline())
# dp[0], dp[2], dp[3]은 규칙을 적용할 시 index가 범위를 벗어날 수 있어 직접 저장
dp[0], dp[1] = stairs[0], stairs[0] + stairs[1]
dp[2] = max(stairs[1]+stairs[2], stairs[0]+stairs[2])

# max(한 계단, 두 계단) 두가지 경우 중 큰 값을 dp[i]에 할당한다.
for i in range(3,N):
    dp[i] = max(dp[i-3] + stairs[i] + stairs[i-1], dp[i-2] + stairs[i])
# dp[N-1] 출력
print(dp[N-1])