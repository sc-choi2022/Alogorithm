import sys

# 배열의 크기 N, M
N, M = map(int, sys.stdin.readline().split())

# 2차원 배열 numbers
numbers = [[0] * (M+1)] + [[0] + list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for ni in range(1, N+1):
    for nj in range(1, M+1):
        numbers[ni][nj] += numbers[ni][nj-1] + numbers[ni-1][nj] - numbers[ni-1][nj-1]

# 합을 구할 부분의 개수 K
K = int(sys.stdin.readline())

for _ in range(K):
    # 좌표 i, j, x, y
    i, j, x, y = map(int, sys.stdin.readline().split())
    # 배열의 합을 출력
    print(numbers[x][y] - numbers[x][j-1] - numbers[i-1][y] + numbers[i-1][j-1])