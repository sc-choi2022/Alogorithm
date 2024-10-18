import sys

def dfs(zero):
    global flag, sudoku

    if flag:
        return

    if zero == len(zeros):
        sudoku = [list(map(str, sudoku[si])) for si in range(9)]
        for sudo in sudoku:
            print(''.join(sudo))
        flag = True
        return
    else:
        (i, j) = zeros[zero]
        numbers = check(i, j)

        for num in numbers:
            sudoku[i][j] = num
            dfs(zero + 1)
            sudoku[i][j] = 0

def check(i, j):
    full = [f for f in range(1, 10)]

    for k in range(9):
        if sudoku[i][k] in full:
            full.remove(sudoku[i][k])
        if sudoku[k][j] in full:
            full.remove(sudoku[k][j])

    i, j = (i//3)*3, (j//3)*3

    for bi in range((i//3)*3, (i//3)*3+3):
        for bj in range((j//3)*3, (j//3)*3+3):
            if sudoku[bi][bj] in full:
                full.remove(sudoku[bi][bj])

    return full

# 스도쿠 퍼즐을 저장하는 배열 sudoku
sudoku = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(9)]
# 0인 위치를 저장하는 배열 zeros
zeros = []

for si in range(9):
    for sj in range(9):
        if sudoku[si][sj] == 0:
            zeros.append((si, sj))

flag = False
dfs(0)