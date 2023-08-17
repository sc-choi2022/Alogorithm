import sys

# 궁수를 배치하는 함수 archer
def archer(cnt, lst):
    if cnt == 3:
        attack(lst)
        return
    for ai in range(N):
        for aj in range(N):
            if (ai, aj) not in lst:
                # board[ai][aj] = 2
                lst.append((ai, aj))
                archer(cnt+1, lst)
                # board[ai][aj] = 0
                lst.pop()

# 궁수가 공격하는 함수 attack
def attack(lst):
    global answer
    # 궁수의 공격으로 제거된 적의 수
    tmp_cnt = 0
    now = enemy[::]
    tmp = set()
    while now:
        # 궁수가 공격
        for l in lst:
            t1, t2 = (-1, -1), -1
            for n in now:
                L = abs(l[0]-n[0])+abs(l[1]-n[1])
                if L <= D:
                    if t1 == (-1, -1):
                        t1 = n
                        t2 = L
                    elif t2 > L:
                        t1 = n
                        t2 = L
                    elif t2 == L and t1[0] > n[0]:
                        t1 = n
                        t2 = L
            if t1 != (-1, -1):
                tmp.add(t1)
        for t in tmp:
            now.remove(t)
        # 적이 이동
        for n in now:
            if n[0] + 1 < N:
                tmp.add(n)
        now = list(tmp)
    answer = max(answer, tmp_cnt)

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
print(answer)