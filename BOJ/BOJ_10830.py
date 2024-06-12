import sys

def power():
    T = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            T[i][j] = fill(i, j)
    return T

def fill(fi, fj):
    tmp = 0
    for f in range(N):
        tmp += A[fi][f]*C[fj][f]
    return tmp%1000

# 행렬 A의 크기 N, 제곱하는 수 B
N, B = map(int, sys.stdin.readline().split())
# 행렬 A
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

C = list(map(list, zip(*A)))

for _ in range(B-1):
    A = power()

for a in A:
    print(*a)