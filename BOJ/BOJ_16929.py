import sys

def cycle(ci, cj, d):
    global answer

    if (ci, cj, d) == (si, sj, 3):
        if L[0] == L[2] and L[1] == L[3]:
            answer = 'Yes'
            return
    for dd in (0, 1):
        ni, nj = D[dd]

# 게임판의 크기 N, M
N, M = map(int, sys.stdin.readline().split())
# 게이판의 점의 색을 저장하는 배열 dots
dots = [list(sys.stdin.readline().rstrip()) for _ in range(N)]

# 방향 칸수를 저장하는 배열 L
L = [0] * 4
# 방향을 저장하는 딕셔너리 D
D = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}

answer = 'No'

for i in range(N-1):
    for j in range(M-1):
        si, sj = i, j
        cycle(i, j, 0)

        if answer == 'Yes':
            print(answer)
            sys.exit()
print(answer)