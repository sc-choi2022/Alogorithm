import sys

# 자두가 떨어지는 시간 T초, 움직이는 횟수 W
T, W = map(int, sys.stdin.readline().split())
# 자두가 떨어지는 나무의 번호를 저장하는 배열 plum
plum = [int(sys.stdin.readline()) for _ in range(T)]
dp = [[0]*T for _ in range(T)]
dp[0][0], dp[0][1] = plum[0]%2, plum[0]//2

for t in range(1, T):
    for w in range(1, W):
        