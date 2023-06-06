import sys

# 행렬 A의 크기 N, M
N, M = map(int, sys.stdin.readline().split())
# 행렬 A
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# 행렬 B의 크기 M, K
M, K = map(int, sys.stdin.readline().split())
# 행렬 B
B = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
# AxB 값을 저장하는 배열 C
C = [[0]*K for _ in range(N)]

for i in range(N):
    for j in range(M):
        for k in range(K):
            C[i][k] += A[i][j] * B[j][k]
# 행렬 C의 원소를 공백으로 구분하여 출력
for c in C:
    print(*c)