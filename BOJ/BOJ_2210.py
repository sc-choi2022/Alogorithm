import sys

def dfs(x, y, number):
    if len(number) == 6:
        if number not in result:
            result.add(number)
        return

    for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
        ni, nj = x+di, y+dj
        if 0 <= ni < 5 and 0 <= nj < 5:
            dfs(ni, nj, number + matrix[ni][nj])

# 주어지는 숫자판 matrix
matrix = [list(sys.stdin.readline().rstrip().split()) for _ in range(5)]

# 만들 수 있는 수들 저장하는 셋 result
result = set()
# 모든 임의의 위치에서 함수 dfs를 시작
for i in range(5):
    for j in range(5):
        dfs(i, j, matrix[i][j])
# 만들 수 있는 수들의 개수를 출력
print(len(result))