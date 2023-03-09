import sys

# 상자의 개수 N
N = int(sys.stdin.readline())
# N개의 상자들의 크기를 저장할 배열 boxes
boxes = list(map(int, sys.stdin.readline().split()))
# 다이나믹프로그래밍을 위한 배열 dp
dp = [1] * N

for i in range(N):
    for j in range(i):
        if boxes[i] > boxes[j]:
            dp[i] = max(dp[i], dp[j] + 1)
# 넣을 수 있는 최대의 상자 개수를 출력
print(max(dp))