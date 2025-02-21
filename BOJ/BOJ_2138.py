import sys

def change(status, cnt):
    for i in range(1, N-1):
        if status[i-1] != goal[i-1]:
            cnt += 1
            for j in range(i-1, i+2):
                status[j] = not status[j]

    # 마지막 스위치를 눌러야하는 경우
    if status[N-1] != goal[N-1]:
        cnt += 1
        status[N-2] = not status[N-2]
        status[N-1] = not status[N-1]

    # 만들고자하는 전구들의 상태인 경우 cnt
    if status == goal:
        return cnt
    # 만들어지지 못한 경우 -1
    else:
        return -1

# 스위치의 개수 N
N = int(sys.stdin.readline())
# 전구의 현재 상태 배열 now
now = list(map(bool, map(int, sys.stdin.readline().rstrip())))
# 만들고자 하는 전구의 상태 배열 goal
goal = list(map(bool, map(int, sys.stdin.readline().rstrip())))

# 0번 스위치를 누른 상태를 저장한 배열 zero
zero = now[::]
zero[0], zero[1] = not zero[0], not zero[1]

# 스위치를 누를 필요가 없는 경우
if now == goal:
    print(0)
else:
    # 0번 스위치를 제외하고 스위치를 변경
    cnt = change(now, 0)

    # 0번 전구의 변경 없이 전구를 완성한 경우 cnt 출력
    if cnt != -1:
        print(cnt)
    else:
        # 0번 전구을 포함하여 스위치를 변경
        cnt = change(zero, 1)
        # 최소 스위치 조작 횟수를 출력, 불가능한 경우에는 -1을 출력
        print(cnt)