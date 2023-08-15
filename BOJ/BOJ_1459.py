from collections import deque
import sys

# 집의 위치 X, Y, 한 블록 가는데 걸리는 시간 W, 대각선으로 한 블록을 가로지르는 시간 S
X, Y, W, S = map(int, sys.stdin.readline().split())
# 가로, 세로로만 이동하는 경우 W1
W1 = (X+Y)*W
# 대각선으로만 이동하는 경우 W2
if not (X+Y)%2:
    W2 = max(X, Y) * S
# 대각선으로 이동 + 가로, 세로 이동 1번
else:
    W2 = (max(X, Y)-1) * S + W
# 평행이동 + 대각선 이동 W3
W3 = (min(X, Y) * S) + (abs(X-Y)*W)

# 세준이가 집에가는데 걸리는 최소시간을 출력
print(min(W1, W2, W3))