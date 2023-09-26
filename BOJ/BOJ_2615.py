import sys
def check():
    for i in range(15):
        for j in range(15):
            if gomoku[i][j]:
                for di, dj in (0, 1), (1, 1), (1, 0), (-1, 1):
                    flag = 0
                    if gomoku[i][j] == gomoku[i+di][j+dj]:
                        if ((i, j) == (0, 0)) or (i == 0 and (di, dj) == (1, 0)) or (j == 0 and (di, dj) in ((1, 1), (1, 0), (-1, 1))):
                            flag = six(i, j, di, dj)
                        if gomoku[i][j] != gomoku[i-di][j-dj]:
                            flag = six(i, j, di, dj)
                        if flag:
                            return (gomoku[i][j], i, j)
    return 0

def six(si, sj, di, dj):
    for k in range(1, 5):
        if gomoku[si + (k - 1) * di][sj + (k - 1) * dj] != gomoku[si + k * di][sj + k * dj]:
            return False
    # 5개만 확인하면 되는 경우
    if ((si, sj) == (14, 14) and (di, dj) == (1, 1)) or (si == 14 and (di, dj) == (1, 0)) or (sj == 14 and (di, dj) == (0, 1)):
        return True
    # 6번째 돌의 확인이 필요한 경우
    if gomoku[si][sj] == gomoku[si+5*di][sj+5*dj]:
        return False
    return True

gomoku = [list(map(int, sys.stdin.readline().split())) for _ in range(19)]
result = check()
if result == 0:
    print(result)
else:
    print(result[0])
    print(result[1]+1, result[2]+1)