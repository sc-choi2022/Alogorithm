import sys
sys.stdin = open('sample_input.txt')

def dfs(n, ci, cj, visit, cnt):
    global ans, si, sj
    if n>3: # 종료조건
        return
    if n == 3 and (ci, cj) == (si, sj) and ans < cnt:
        ans = cnt
        return
    for k in range(n, n+2):
        ni, nj = ci + di[k], cj + dj[k]
        if 0<= ni <N and 0<= nj < N and des[ni][nj] not in visit:
            # dfs(k, ni, nj, visit + [des[ni][nj]], cnt + 1)
            visit.append(des[ni][nj])
            dfs(k, ni, nj, visit, cnt + 1)
            visit.pop()

T = int(input())
di = (1, 1, -1, -1, 1)
dj = (-1, 1, 1, -1, -1)
for case in range(1, T+1):
    N = int(input())
    des = [list(map(int, input().split())) for _ in range(N)]
    ans = -1

    for si in range(0, N-2):
        for sj in range(1, N-1):
            dfs(0, si, sj, [], 0)

    print(f'#{case} {ans}')