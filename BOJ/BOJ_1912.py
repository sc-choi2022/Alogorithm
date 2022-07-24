import sys

# 정수 N
N = int(sys.stdin.readline())
# n개의 정수로 이루어진 수열을 담은 리스트 numbers
numbers = list(map(int, sys.stdin.readline().split()))
# 인덱스의 위치에서 연속한 합 중 가장 큰 합을 담을 리스트 dp
dp = [0]*N
# dp[0]은 numbers[0]을 할당
dp[0] = numbers[0]

for i in range(1, N):
    # dp[i]에 numbers[i]의 값과 dp[i-1] + numbers[i] 중 큰 값을 할당
    dp[i] = max(numbers[i], dp[i-1] + numbers[i])
# dp의 최댓값을 출력
print(max(dp))