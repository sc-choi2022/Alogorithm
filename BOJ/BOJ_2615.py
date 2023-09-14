import sys

def place():
    for i in range(15):
        for j in range(15):
            if gomoku[i][j]:
                for di, dj in (1, 0), (0, 1), (1, 1), (1, -1):
                    for k in range(1, 5):
                        ni, nj = i + k*di, j + k*dj
                        if gomoku[i][j] != gomoku[ni][nj]:
                            break
                    else:
                        print(gomoku[i][j])
                        print(i+1, j+1)
                        return True
    return False

gomoku = [list(map(int, sys.stdin.readline().split())) for _ in range(19)]
answer = place()
if not answer:
    print(0)