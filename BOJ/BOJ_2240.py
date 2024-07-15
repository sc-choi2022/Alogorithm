import sys

# 자두가 떨어지는 시간 T초, 움직이는 횟수 W
T, W = map(int, sys.stdin.readline().split())
# 자두가 떨어지는 나무의 번호를 저장하는 배열 plum
plum = [0] + [int(sys.stdin.readline()) for _ in range(T)]
dp = [[0]*(W+1) for _ in range(T+1)]
dp[1][0], dp[1][1] = plum[1]%2, plum[1]//2

for t in range(2, T + 1):
    for w in range(2, W + 1):
        tmp = plum[t]%2 if w%2 == 0 else plum[t]//2
        dp[t][w] = max(dp[t-1][0:2+1]) + tmp
    print(max(dp[-1]))