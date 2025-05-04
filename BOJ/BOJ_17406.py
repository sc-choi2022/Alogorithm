from copy import deepcopy
import sys

def turn():
    global A

    # 회전을 저장하는 배열 B
    B = deepcopy(A)
    # 회전하는 범위 (si, sj) (ei, ej)
    si, sj = r-s, c-s
    ei, ej = r+s, c+s
    for ii in range(s):
        # 시작범위 (ci, cj), 마지막범위 (fi, fj)
        ci, cj = si + ii, sj + ii
        fi, fj = ei - ii, ej - ii

        i, j = ci, cj
        for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
            while True:
                ni, nj = i+di, j+dj
                # 범위 내의 위치인 경우
                if ci <= ni <= fi and cj <= nj <= fj:
                    B[ni][nj] = A[i][j]
                    i, j = ni, nj
                else:
                    break
    # 회전 연산을 진행한 배열 B를 배열 A로 저장
    A = B

# 배열 A의 크기 N, M, 회전 연산의 개수 K
N, M, K = map(int, sys.stdin.readline().split())
# 배열 A
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for _ in range(K):
    # 회전 연산의 세 정수 r, c, s
    r, c, s = map(int, sys.stdin.readline().split())
    r, c = r-1, c-1
    turn()

# 배열 A의 값의 최솟값 answer
answer = 1e8

for s in range(N):
    answer = min(answer, sum(A[s]))
# 배열 A의 최솟값을 출력
print(answer)