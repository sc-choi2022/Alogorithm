import sys

# 크기 S, 모니터에 나타내야할 수 N
S, N = sys.stdin.readline().rstrip().split()
S = int(S)

lcd = [['']*(S+2) for _ in range(2*S+3)]
