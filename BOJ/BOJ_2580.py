import sys
# 0을 포함하는 스도쿠를 sudoku리스트에 담는다.
sudoku = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]

# sudoku에 값이 0인 위치를 담을 리스트 zeros
zeros = []
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            zeros.append((i, j))

# i,j가 행열, 3x3 위치에서 확인하여 사용하지 않은 숫자를 리턴하는 함수
def check(i, j):
    full = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # 행과 열을 확인하는 for문
    for k in range(9):
        # 행을 확인하는 if문
        if sudoku[i][k] in full:
            full.remove(sudoku[i][k])
        # 열을 확인하는 if문
        if sudoku[k][j] in full:
            full.remove(sudoku[k][j])

    # 3x3 검사
    # i,j 위치를 3x3을 기준으로 나눴을 때 (1,1)의 위치에서 검사를 시작
    # 이를 위해 3의 몫을 구하고 3을 곱한다.
    i = (i // 3) * 3
    j = (j // 3) * 3
    for box1 in range(i, i + 3):
        for box2 in range(j, j + 3):
            if sudoku[box1][box2] in full:
                full.remove(sudoku[box1][box2])
    # full에서 remove되지 않은 숫자들을 return 한다.
    return full

# 백트래킹을 활용하는 def
def dfs(zero):
    global flag

    # flag가 True라면 return
    if flag:
        return

    # zeros가 비어 있다면 스도쿠를 출력하고
    if zero == len(zeros):
        for su in sudoku:
            print(*su)
        # flag를 True로 바꾼다.
        flag = True
        return
    # zeros가 비어있지 안하면
    else:
        # 0인 첫번째 위를 받아서 check 함수를 numbers에 담는다.
        (i, j) = zeros[zero]
        numbers = check(i, j)

        # numbers의 각 숫자를 재귀함수를 통해서 (i,j)위치에 넣어보고 다시 0으로 초기화한다.
        for num in numbers:
            sudoku[i][j] = num
            dfs(zero + 1)
            sudoku[i][j] = 0

# flag를 False로 초기화
flag = False
# dfs에 0을 값으로 실행
dfs(0)