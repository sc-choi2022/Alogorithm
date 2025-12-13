import sys

def solution(A, S):
    idx, cnt = 0, 0
    for i in range(N):
        if S[idx] == 'W' and S[idx-1] == 'E':
            cnt += 1
    return cnt

N = int(sys.stdin.readline())
cmd = sys.stdin.readline().rstrip()
answer = sol(N, cmd)