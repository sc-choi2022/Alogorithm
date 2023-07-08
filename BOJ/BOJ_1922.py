import sys

# 컨퓨터의 수 N
N = int(sys.stdin.readline())
# 연결할 수 있는 선의 수 M
M = int(sys.stdin.readline())
parent = [x for x in range(N+1)]
