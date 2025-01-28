import sys

def square(A, B):
    if B == 1:
        for i in range(len(A)):
            for j in range(len(A)):
                A[i][j] %= 1000
        return A
    tmp = square(A, B//2)

    if B%2:
        return mul(mul(tmp, tmp), A)
    else:
        return mul(tmp, tmp)

def mul(U, V):
    L = len(U)
    Z = [[0]*L for _ in range(L)]

    for i in range(L):
        for j in range(L):
            e = 0
            for k in range(L):
                e += U[i][k] * V[k][j]
            Z[i][j] = e%1000
    return Z

# 행렬 A의 크기 N, 제곱하는 수 B
N, B = map(int, sys.stdin.readline().split())
# 행렬 A
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 행렬 A를 제곱한 결과
answer = square(A, B)

for a in answer:
    print(*a)