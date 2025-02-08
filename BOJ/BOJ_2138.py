import sys

def change():
    return

# 스위치의 개수 N
N = int(sys.stdin.readline())
# 전구의 현재 상태 배열 now
now = list(sys.stdin.readline().rstrip())
# 만들고자 하는 전구의 상태 배열 goal
goal = list(sys.stdin.readlin().rstrip())

# 0번 스위치를 누른 상태를 저장한 배열 zero
zero = now[::]
zero[0], zero[1] = not zero[0], not zero[1]

if now == goal:
    print(0)
else:
    cnt = change(now, 0)
    if cnt == -1:
        print(cnt)
    else:
        cnt = change(zero, 1)
        print(cnt if cnt else -1)