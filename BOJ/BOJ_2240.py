import sys

# 자두가 떨어지는 시간 T초, 움직이는 횟수 W
T, W = map(int, sys.stdin.readline().split())
# 자두가 떨어지는 나무의 번호를 저장하는 배열 plum
plum = [0] + [int(sys.stdin.readline()) for _ in range(T)]
# dp[T][W] = T동안 W만큼 이동시 최대 자두개수를 저장하는 배열 dp
dp = [[0]*(W+1) for _ in range(T+1)]
dp[1][0], dp[1][1] = plum[1]%2, plum[1]//2

for t in range(2, T + 1):
    # t-1초의 최대 자두개수 tmp
    tmp = dp[t-1][0]
    for w in range(W + 1):
        tmp = max(tmp, dp[t-1][w])
        # 현재 자두의 개수
        # t초에 1번 나무 아래 있는 경우 plum[t]%2
        # t초에 2번 나무 아래 있는 경우 plum[t]//2
        P = plum[t]%2 if w%2 == 0 else plum[t]//2
        # t-1동안 w번 이하로 이동시 최대자두의 개수 + 현재 자두 개수의 값으로 dp[t][w]을 갱신
        dp[t][w] = tmp + P

# T초동안 최대 W번만 움직이고 받을 수 있는 자두의 최대 개수를 출력
print(max(dp[T]))