from collections import deque
import sys

# 집의 위치 X, Y, 한 블록 가는데 걸리는 시간 W, 대각선으로 한 블록을 가로지르는 시간 S
X, Y, W, S = map(int, sys.stdin.readline().split())
# 세준이가 집에가는데 걸리는 최소시간 time
time = (X+Y) * W

# 세준이가 집에가는데 걸리는 최소시간을 출력
print(time)