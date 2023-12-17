from itertools import permutations
import sys

# 이닝 수 N
N = int(sys.stdin.readline())
# 얻을 수 있는 최대 점수 score
score = 0
# 이닝의 점수를 저장하는 배열 innings
innings = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for permu in list(permutations(range(1,9), 8)):
    # 1번 선수는 고정으로 4번타자 이므로 순서에 맞춰 정해준다.
    permu = permu[:3] + [0] + permu[3:]
    #

    # 현재 선수순서로 이닝 진행시 점수 now
    now = 0
    # 각 베이스의 선수상황을 저장하는 plates
    plates = [0, 0, 0, 0]

    while True:
        # 아웃이 3번이면 이닝이 끝난다.
        if out == 3:
            break