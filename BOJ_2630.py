import sys

def sol(x, y, N):
    global cnt0, cnt1
    color = paper[x][y]
    for i in range(x, x + N):
        for j in range(y, y + N):
            if color != paper[i][j]:
                sol(x, y, N//2)
                sol(x, y + N//2, N//2)
                sol(x + N//2, y, N//2)
                sol(x + N//2, y + N//2, N//2)
                return
    if color == 0:
        cnt0 += 1
    else:
        cnt1 += 1

N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] 

cnt0, cnt1 = 0, 0
sol(0, 0, N)
print(cnt0)
print(cnt1)