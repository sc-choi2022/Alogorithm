from copy import deepcopy
import sys

def turn():
    tmp = deepcopy(A)

    for ti in range(r-s-1, r+s):
        for tj in range(c-s-1, c+s):
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