import sys

def check():
    for i in range(19):
        for j in range(19):
            if gomoku[i][j]:
                color = gomoku[i][j]
                for di, dj in (-1, 1), (1, 0), (1, 1), (0, 1):
                    if 0 <= i + di < 19 and 0 <= j + dj < 19 and gomoku[i + di][j + dj] == color:
                        if 0 <= i - di < 19 and 0 <= j - dj < 19 and gomoku[i - di][j - dj] == color:
                            continue
                        flag = cnt(i, j, di, dj)
                        if flag:
                            # 검은색이 이겼을 경우에는 1을, 흰색이 이겼을 경우에는 2
                            # 연속된 다섯 개의 바둑알 중에서 가장 왼쪽에 있는 바둑알의 가로줄 번호와, 세로줄 번호를 순서대로 출력
                            if 0 <= i + 5 * di < 19 and 0 <= j + 5 * dj < 19:
                                if gomoku[i + 5 * di][j + 5 * dj] != color:
                                    return (gomoku[i][j], i+1, j+1)
                                else:
                                    continue
                            else:
                                return (gomoku[i][j], i+1, j+1)
    return 0
# 오목이 5개를 확인하는 함수 cnt
def cnt(i, j, di, dj):
    color = gomoku[i][j]
    for k in range(2, 5):
        if i + k*di < 0 or i + k*di >= 19 or j + k*dj < 0 or j + k*dj >= 19:
            return False
        if gomoku[i + k * di][j + k * dj] != color:
            return False
    return True

# 주어지는 오목 gomoku
gomoku = [list(map(int, sys.stdin.readline().split())) for _ in range(19)]
# 오목의 결과를 저장하는 변수 result
result = check()

# 아직 승부가 결정되지 않았을 경우에는 0을 출력
if result == 0:
    print(result)
else:
    print(result[0])
    print(result[1], result[2])