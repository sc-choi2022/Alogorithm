import sys

# 성의 세로 크기 N과 가로 크기 M
N, M = map(int, sys.stdin.readline().split())
# 성의 경비원 정보를 담을 castle
castle = [list(sys.stdin.readline().strip()) for _ in range(N)]
# castle의 전치행렬 transCastle
transCastle = list(map(list, zip(*castle)))

# 경비원이 없는 행의 개수 row, 열의 개수 column
row, column = 0, 0

# 경비원이 없는 행의 개수 row를 count
for i in range(N):
    if 'X' not in castle[i]:
        row += 1

# 경비원이 없는 열의 개수 column를 count
for j in range(M):
    if 'X' not in transCastle[j]:
        column += 1

# row와 column 중 큰 값을 출력
print(max(row, column))