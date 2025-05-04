from copy import deepcopy
import sys

def turn():
    tmp = deepcopy(A)
    si, sj = r-s, c-s
    ei, ej = r+s, c+s
    for ii in range(s):
        # 시작범위 (ci, cj), 마지막범위 (fi, fj)
        ci, cj = si + ii, sj + ii
        fi, fj = ei - ii, ej - ii
        for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
            while 0 <= ci < fi and 0 <= cj < fj:
                ni, nj = ci + di, cj + dj
                print(ni, nj)
                tmp[ni][nj] = A[ci][cj]
                ci, cj = ni, nj
    for t in tmp:
        print(*t)

# 배열 A의 크기 N, M, 회전 연산의 개수 K
N, M, K = map(int, sys.stdin.readline().split())
# 배열 A
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for _ in range(K):
    # 회전 연산의 세 정수 r, c, s
    r, c, s = map(int, sys.stdin.readline().split())
    r, c = r-1, c-1
    turn()


answer = 1e8
for i in range(N):
    answer = min(answer, sum(A[i]))

print(answer)