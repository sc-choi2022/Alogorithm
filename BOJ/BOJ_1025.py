import sys

N, M = map(int, sys.stdin.readline().split())
numbers = [list(sys.stdin.readline().rstrip()) for _ in range(N)]

answer = -1

for i in range(N):
    for j in range(M):
        for row in range(-N, N):
            for col in range(-M, M):
                S = ''
                x, y = i, j
                if row == 0 and col == 0:
                    continue
                while 0 <= x < N and 0 <= y < M:
                    S += numbers[x][y]
                    

print(answer)