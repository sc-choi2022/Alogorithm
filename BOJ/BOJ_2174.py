import sys

def do(order):
    global ci, cj, direct, flag
    if order == 'F':
        for _ in range(cnt):
            di, dj = direction[d]
            if 0 <= ci + di < B and 0 <= cj + dj < A:
                ci += di
                cj += dj
                if graph[ci][cj]:
                    print(f'Robot {number} crashes into robot {graph[ci][cj]}')
                    flag = True
                    return
            else:
                print(f'Robot {number} crashes into the wall')
                flag = True
                return
    else:
        tmp = cnt%4
        current = move.index(direct)
        if order == 'L':
            direct = move[current-tmp]
        else:
            direct = move[(current+tmp)%4]

# 땅의 크기 가로A, 세로 B
A, B = map(int, sys.stdin.readline().split())
# 로봇의 개수 N, 명령 개수 M
N, M = map(int, sys.stdin.readline().split())
# 로봇들의 위치를 저장하는 딕셔너리 robots
robots = {}

# 방향을 담을 딕셔너리 direction
direction = {'E':(0,1), 'W':(0,-1), 'S':(1,0), 'N':(-1,0)}
# 명령에 따른 방향을 저장하는 배열 move
move = ['N', 'E', 'S', 'W']

graph = [[0]*A for _ in range(B)]

flag = False

for i in range(N):
    # 로봇의 위치 x, y, 방향 d
    x, y, d = sys.stdin.readline().rstrip().split()
    robots[i+1] = (B-int(y), int(x)-1, d)
    graph[robots[i+1][0]][robots[i+1][1]] = i + 1

for _ in range(M):
    # 명령을 내리는 로봇 number, 명령의 종류 order, 명령의 횟수 cnt
    number, order, cnt = sys.stdin.readline().rstrip().split()
    number = int(number)
    cnt = int(cnt)

    ci, cj, direct = robots[number]
    graph[ci][cj] = 0
    do(order)
    if flag:
        break
    robots[number] = (ci, cj, direct)
    graph[ci][cj] = number
else:
    print('OK')