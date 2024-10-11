import sys

# 영토의 크기 N, M
N, M = map(int, sys.stdin.readline().split())

# 구역 내에 살고 있는 사람 수를 저장하는 배열 numbers
numbers = [[0]*(M+1)] + [[0] + list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for i in range(1, N+1):
    for j in range(1, M+1):
        numbers[i][j] += numbers[i][j-1] + numbers[i-1][j]-numbers[i-1][j-1]

# 직사각형 범위의 개수 K
K = int(sys.stdin.readline())

for _ in range(K):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    # 주어진 직사각형 범위 내에 살고 있는 사람 수의 합을 출력
    print(numbers[x2][y2] - numbers[x1-1][y2] - numbers[x2][y1-1] + numbers[x1-1][y1-1])