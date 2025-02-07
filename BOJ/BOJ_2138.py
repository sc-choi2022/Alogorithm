import sys

def test():
    cnt = 0
    for i in range(1, N-1):
        if now[i-1] != goal[i-1]:
            cnt += 1
            for j in range(i-1, i+2):
                now[j] = not now[j]
    if now[N-1] != goal[N-1]:
        cnt += 1
        now[N-2] = not now[N-2]
        now[N-1] = not now[N-1]
    if now == goal:
        return cnt
    else:
        return -1

# 스위치의 개수 N
N = int(sys.stdin.readline())
# 전구의 현재 상태 배열 now
now = list(sys.stdin.readline().rstrip())
# 만들고자 하는 전구의 상태 배열 goal

on = off[::]
on[0] = not on[0]
on[1] = not on[1]

if off == goal:
    print(0)