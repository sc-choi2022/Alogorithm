import sys

pascal = [[1 for _ in range(i)] for i in range(1, 31)]

for j in range(2, 30):
    for k in range(1, i):
        pascal[j][k] = pascal[j-1][k-1] + pascal[j-1][k]

# N번째 행의 K번째 수
N, K = map(int, sys.stdin.readline().split())
print(pascal[N-1][K-1])