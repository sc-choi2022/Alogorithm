import sys

def fill(n, ci, cj):
    if n == 1:
        stars[ci][cj] = '*'
        return
    L = 4 * n - 3

    for i in range(L):
        stars[cj][ci+i] = '*'
        stars[cj+i][ci] = '*'
        stars[cj+L-1][ci+i] = '*'
        stars[cj+i][ci+L-1] = '*'
    fill(n-1, ci+2, cj+2)

# 기준이 되는 정수 N
N = int(sys.stdin.readline())

stars = [[' ' for _ in range(4*N-3)] for _ in range(4*N-3)]

fill(N, 0, 0)

for star in stars:
    print(''.join(star))