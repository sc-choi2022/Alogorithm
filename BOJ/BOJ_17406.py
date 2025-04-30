from copy import deepcopy
import sys

def turn():
    tmp = deepcopy(A)
    si, sj = r-1, c-1
    ei, ej = r+s-1, c+s-1
    for ii in range(s):
        ci, cj = si + ii, sj + ii
        fi, fj = ei - ii, ej - ii
        for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
            ni, nj = ci+di, cj+dj
            while True:
                return 

# 배열 A의 크기 N, M, 회전 연산의 개수 K
N, M, K = map(int, sys.stdin.readline().split())
# 배열 A
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for _ in range(K):
    # 회전 연산의 세 정수 r, c, s
    r, c, s = map(int, sys.stdin.readline().split())


answer = 1e8
for i in range(N):
    answer = min(answer, sum(A[i]))

print(answer)