import sys

# 초기 비용 H, 투자 기간 Y
H, Y = map(int, sys.stdin.readline().split())
#  해의 최대 자산을 저장하는 배열 dp
dp = [0] * (Y+1)
dp[0] = H
# 이율 정보를 저장하는 딕셔너리 interest
interest = {1: 1.05, 3: 1.2, 5: 1.35}

for i in range(1, Y+1):
    for j in (1, 3, 5):
        if i-j >= 0:
            dp[i] = max(dp[i], int(dp[i-j]*interest[j]))

# 가장 많은 이득을 얻었을 때의 총 자산을 소수점을 모두 버리고 정수로 출력
print(dp[Y])