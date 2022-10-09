import sys

N, M = map(int, sys.stdin.readline().split())
square = [list(sys.stdin.readline().strip()) for _ in range(N)]
# trans = list(zip(*square))
#
# for i in range(N):
#     for j in range(M):
#         tmp = square[i][j]
#         if tmp in

check = min(N, M)
answer = 0
for i in range(N):
    for j in range(M):
        for k in range(check):
            if ((i + k) < N) and ((j + k) < M) and (square[i][j] == square[i][j + k] == square[i + k][j] == square[i + k][j + k]):
                answer = max(answer, (k + 1) **2)
print(answer)