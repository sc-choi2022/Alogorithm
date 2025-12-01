import sys

def dfs():
    return 

N, M = map(int, sys.stdin.readline().split())
numbers = [list(sys.stdin.readline().rstrip()) for _ in range(N)]

answer = -1

for i in range(N):
    for j in range(N):
        for row in range(-N, N):
            for col in range(-M, M):
                continue