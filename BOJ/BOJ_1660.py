import sys

# 대포알의 개수 N
N = int(sys.stdin.readline())
balls = []
B = 0
i = 1

while B < N:
    B += (i * (i+1))//2
    balls.append(B)
    i += 1
