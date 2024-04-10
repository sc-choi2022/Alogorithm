from collections import deque
import sys

# 카드와 기술의 개수 N
N = int(sys.stdin.readline())
# 현재 카드의 상태 card
card = deque([i for i in range(N, 0, -1)])

# 기술이 번호를 저장하는 배열 skills
skills = reversed(list(map(int, sys.stdin.readline().split())))

for skill in skills:
    if skill == 1:
        continue
    elif skill == 2:
        continue
    else:
        continue