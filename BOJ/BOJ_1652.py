import sys

def func(lst):
    cnt = 0
    for i in range(N):
        tmp = 0
        for j in range(N):
            if lst[i][j] == '.':
                tmp += 1
            else:
                if tmp >= 2:
                    cnt += 1
                    tmp = 0
                else:
                    tmp = 0
        if tmp >= 2:
            cnt += 1
    return cnt

# 방의 크기 N
N = int(sys.stdin.readline())
# 방의 상태 room
room = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
# 세로방향을 확인하기 위한 room의 전치 roomT
roomT = list(map(list, zip(*room)))

# 가로로 누울 수 있는 자리와 세로로 누울 수 있는 자리의 개수를 출력
print(func(room), func(roomT))