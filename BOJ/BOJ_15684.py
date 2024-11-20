import sys

def garo(si, sj, cnt):
    global answer

    if cnt >= answer:
        return
    elif play():
        answer = min(answer, cnt)
        return
    elif cnt == 3:
        return

    for ni in range(si, H):
        S = sj if ni == si else 0
        for nj in range(S, N-1):
            if not lader[ni][nj]:
                lader[ni][nj] = 1
                garo(ni, nj+2, cnt+1)
                lader[ni][nj] = 0

def play():
    for pj in range(N):
        now = pj
        for pi in range(H):
            if lader[pi][now]:
                now += 1
            elif now and lader[pi][now-1]:
                now -= 1
        if now != pj:
            return False
    return True

# 세로선의 개수 N, 가로선의 개수 M, 위치의 개수 H
N, M, H = map(int, sys.stdin.readline().split())
# 가로선의 위치를 저장하는 배열 lader
lader = [[0] * N for _ in range(H)]

for _ in range(M):
    # 가로선의 위치 정보 a, b
    a, b = map(int, sys.stdin.readline().split())
    lader[a-1][b-1] = 1

# 추가해야하는 가로선의 개수 answer를 4로 초기화
answer = 4
garo(0, 0, 0)

# 가로선 개수의 최솟값을 출력
# 정답이 3보다 큰 값이면 -1을 출력
print(-1 if answer > 3 else answer)