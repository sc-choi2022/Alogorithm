from itertools import permutations
import sys

# 이닝 수 N
N = int(sys.stdin.readline())
# 얻을 수 있는 최대 점수 score
score = 0
# 이닝의 점수를 저장하는 배열 innings
innings = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# 1번 선수를 제외한 선수들의 모든 라인업을 저장하는 배열 permu
permu = list(permutations(range(1,9), 8))

for p in permu:
    # 1번 선수는 고정으로 4번타자 이므로 순서에 맞춰 정해준다.
    p = p[:3] + [0] + p[3:]

    # 배열 p의 현재 선수 위치 batter
    batter = 0
    # 현재 선수순서로 이닝 진행시 점수 now
    now = 0

    # 이닝의 수
    for i in range(N):
        # 아웃카운트 out
        out = 0
        # 각 베이스의 선수상황을 저장하는 plates
        plates = [0, 0, 0]

        while True:
            if out == 3:
                break

            # i번째 이닝의 타자 batter의 정보를 저장하는 변수 hit
            hit = innings[i][p[batter]]

            # 아웃을 당한 경우
            if hit == 0:
                out += 1
            # 안타인 경우
            elif hit == 1:
                # 3루의 값을 스코어에 저장해준다.
                now += plates[2]
                # 베이스플레이트 상황을 갱신
                print(plates)
                plates = [1] + plates[:2]
                print(plates)
                print('---------------------------------')