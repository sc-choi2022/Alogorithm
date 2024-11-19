import sys

def plus(cnt, x, y):
    global answer

    if answer <= cnt:
        return
    elif play():
        answer = min(answer, cnt)
        return
    elif cnt == 3:
        return

    for pi in range(x, H):
        if pi == x:
            k = y
        else:
            k = 0
        for pj in range(k, N-1):
            if not garo[pi][pj]:
                garo[pi][pj] = 1
                plus(cnt+1, pi, pj+2)
                garo[pi][pj] = 0

def play():
    for jj in range(N):
        now = jj
        for ii in range(H):
            if garo[ii][now]:
                now += 1
            elif now > 0 and garo[ii][now-1]:
                now -= 1
        if now != jj:
            return False
    return True

# 세로선의 개수 N, 가로선의 개수 M, 세로선마다 가로선을 놓을 수 있는 위치 개수 H
N, M, H = map(int, sys.stdin.readline().split())
garo = [[0]*N for _ in range(H)]
answer = 4

for l in range(M):
    a, b = map(int, sys.stdin.readline().split())
    garo[a-1][b-1] = 1

plus(0, 0, 0)
print(answer if answer <= 3 else -1)