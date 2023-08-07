import sys

# 궁수를 배치하는 함수 archer
def archer(cnt, lst):
    if cnt == 3:
        attack(lst)
        return
    for ai in range(N):
        for aj in range(N):
            if not board[ai][aj]:
                board[ai][aj] = 2
                lst.append((ai, aj))
                archer(cnt+1, lst)
                board[ai][aj] = 0
                lst.pop()

# 궁수가 공격하는 함수 attack
def attack(lst):
   while True:
        reject = set()
        for castle in lst:
            able = (-1, -1)
            for e in enemy:
                if abs(castle[0]-e[0]) + abs(castle[1]-e[1]) <= D:
                    if able == (-1, -1):
                        able = e
                    else:
                        if abs(castle[0]-e[0]) + abs(castle[1]-e[1]) <= abs(castle[0]-able[0]) + abs(castle[1]-able[1]) and e[1] < able[1]:
                            able = e
            reject.add(e)

        for r in reject:
            enemy.remove(r)


# 격자판 행의 수 N, 열의 수 M, 궁수의 공격 거리 제한 D
N, M, D = map(int, sys.stdin.readline().split())
# 격자판 board
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# 궁수의 공격으로 제거할 수 있는 적의 최대 수 answer
answer = 0
# 적의 위치를 저장하는 배열 enemy
enemy = []

for ei in range(N):
    for ej in range(M):
        if board[ei][ej] == 1:
            enemy.append((ei, ej))
enemy.sort(key=lambda x:(x[1]))
print(enemy)
archer(0, [])