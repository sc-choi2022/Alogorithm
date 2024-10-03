import sys

# 실수의 개수 N
N = int(sys.stdin.readline())
# 실수를 저장하는 배열 numbers
numbers = [float(sys.stdin.readline()) for _ in range(N)]
# 인덱스 위치를 포함한 연속된 수의 최대값을 담을 리스트 dp
dp = [0] * N

for i in range(N):
    dp[i] = max(dp[i-1]*numbers[i], numbers[i])

# 최댓값을 소수점 이하 넷째 자리에서 반올림하여 소수점 이하 셋째 자리까지 출력
print('{:.3f}'.format(max(dp)))