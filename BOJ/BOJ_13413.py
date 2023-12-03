import sys

# 테스트 케이스 T
T = int(sys.stdin.readline())

for _ in range(T):
    # 오셀로 말의 개수 N
    N = int(sys.stdin.readline())
    # 오셀로 말의 초기 상태
    origin = sys.stdin.readline().rstrip()
    # 오셀로 말의 목표 상태
    goal = sys.stdin.readline().rstrip()
    # 위치가 다른 말의 개수 cnt
    cnt = 0
    # 초기 상태의 흰색면 oW, 검은면 oB
    oW, oB = 0, 0
    # 목표 상태의 흰색면 gW, 검은면 gB
    gW, gB = 0, 0
    for i in range(N):
        if origin[i] != goal[i]:
            cnt += 1
        if origin[i] == 'W':
            oW += 1
        else:
            oB += 1
        if goal[i] == 'W':
            gW += 1
        else:
            gB += 1
    answer = 0

    print(answer)