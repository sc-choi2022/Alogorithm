from collections import deque
import sys

# 카드와 기술의 개수 N
N = int(sys.stdin.readline())
# 현재 카드의 상태 card
card = deque()

# 기술이 번호를 저장하는 배열 skills
skills = list(map(int, sys.stdin.readline().split()))
skills.reverse()

for i in range(N):
    if skills[i] == 1:
        card.appendleft(i+1)
    elif skills[i] == 2:
        card.insert(1, i+1)
    else:
        card.append(i+1)

# 초기 카드의 상태를 위에서부터 순서대로 출력
print(*card)