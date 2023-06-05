import sys

# 행렬 A의 크기 N, M
N, M = map(int, sys.stdin.readline().split())
# 행렬 A
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
M, K = map(int, sys.stdin.readline().split())
B = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
# B = list(map(list, zip(*B)))

print(A)
print(B)

for i in range(N):
    for j in range(M):
        for k in range(K):
            print(A[i][j]*B[j][k], end=' ')
    print()