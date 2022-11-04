import sys

# 나열된 양의 실수들의 개수 N
N = int(sys.stdin.readline())
# 주어지는 수를 담을 리스트 numbers
numbers = [0] * N
# 인덱스 위치를 포함한 연속된 수의 최대값을 담을 리스트 dp
dp = [0] * N

# 주어지는 수를 numbers에 저장
for i in range(N):
    numbers[i] = float(sys.stdin.readline().strip())

# dp 리스트 갱신
for j in range(N):
    dp[j] = max(dp[j - 1]*numbers[j], numbers[j])

# 최댓값을 소수점 이하 넷째 자리에서 반올림하여 소수점 이하 셋째 자리까지 출력
print('{:.3f}'.format(max(dp)))