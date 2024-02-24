from copy import deepcopy
from itertools import combinations
import sys

# 적을 공격하는 함수 attack
def attack(archers):
    # 각 궁수의 가장 가까운 적을 저장하는 배열 enemy
    enemy = set()

    for cj in archers:
        location = []
        for ai in range(N):
            for aj in range(M):
                if fight[ai][aj] == 1:
                    # 궁수와 적의 위치의 거리 L
                    L = abs(ai-N) + abs(aj-cj)
                    if L <= D:
                        location.append((L, ai, aj))
        location.sort(key=lambda x:(x[0], x[2]))

        if location:
            enemy.add((location[0][1], location[0][2]))
    # 공격받은 적을 게임에서 제외
    for li, lj in enemy:
        fight[li][lj] = 0
    # 제거한 적의 수 return
    return len(enemy)

# 적을 이동시키는 함수 move
def move():
    for mi in range(-1, -N, -1):
        fight[mi] = fight[mi-1]
    fight[0] = [0]*M

# 게임의 종료를 확인하는 함수 check
def check():
    for ci in range(N):
        if sum(fight[ci]):
            return False
    return True

# 행의 수 N, 열의 수 M, 궁수의 공격 거리 제한 D
N, M, D = map(int, sys.stdin.readline().split())
# 격자판의 상태를 저장하는 배열 graph
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# 궁수의 공격으로 제거할 수 있는 적의 최대 수 answer
answer = 0

# 1. 궁수를 배치
for archers in combinations(range(M), 3):
    # 격자판을 상태를 저장하는 배열 fight
    fight = deepcopy(graph)
    # 현재 궁수의 위치에서 제외된 적의 수 cnt
    cnt = 0
    # 적이 있는 동안 반복
    while not check():
        # 2. 적을 공격
        cnt += attack(archers)
        # 3. 적이 이동
        move()
    # answer값 갱신
    answer = max(answer, cnt)
# 궁수의 공격으로 제거할 수 있는 적의 최대 수를 출력
print(answer)