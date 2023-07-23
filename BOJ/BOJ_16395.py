import sys

# N번째 행에 있는 K번째 수 N, K
N, K = map(int, sys.stdin.readline().split())
# 1. N번째 행은 N개의 수
# 2. 첫번째 항은 1이다.
# 3. 두 번째 행부터, 각 행의 양 끝의 값은 1
pascal = [[1]*i for i in range(1, N+1)]

for j in range(1, N):
    for k in range(1, j):
        # 3. 나머지 수의 값은 바로 위 행의 인접한 두 수의 합
        pascal[j][k] = pascal[j-1][k-1] + pascal[j-1][k]
# N번째 행에 있는 K번째 수 출력
print(pascal[N-1][K-1])