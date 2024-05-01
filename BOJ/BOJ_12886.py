from collections import deque
import sys

def bfs():
    queue = deque([(A, B, C)])
    visit.add((A, B, C))

    while queue:
        cA, cB, cC = queue.popleft()

        if (cA, cB, cC) == (N, N, N):
            return 1

        if cA > cB:
            if (cA-cB, cB+cB, cC) not in visit:
                visit.add((cA-cB, cB+cB, cC))
                queue.append((cA-cB, cB+cB, cC))
        if cA > cC:
            if (cA-cC, cB, cC+cC) not in visit:
                visit.add((cA-cC, cB, cC+cC))
                queue.append((cA-cC, cB, cC+cC))
        if cB > cA:
            if (cA+cA, cB-cA, cC) not in visit:
                visit.add((cA+cA, cB-cA, cC))
                queue.append((cA+cA, cB-cA, cC))
        if cB > cC:
            if (cA, cB-cC, cC+cC) not in visit:
                visit.add((cA, cB-cC, cC+cC))
                queue.append((cA, cB-cC, cC+cC))
        if cC > cA:
            if (cA+cA, cB, cC-cA) not in visit:
                visit.add((cA+cA, cB, cC-cA))
                queue.append((cA+cA, cB, cC-cA))
        if cC > cB:
            if (cA, cB+cB, cC-cB) not in visit:
                visit.add((cA, cB+cB, cC-cB))
                queue.append((cA, cB+cB, cC-cB))
    return 0

# 세 그룹의 돌의 개수 A, B, C
A, B, C = map(int, sys.stdin.readline().split())

# 돌이 같은 개수로 만들 수 없는 경우
if (A + B + C)%3:
    print(0)
else:
    # 같은 개수가 되는 정수 N
    N = (A + B + C) // 3
    # 개수가 나누어진 경우를 저장하는 배열 visit
    visit = set()
    # 돌을 같은 개수로 만들 수 있으면 1을, 아니면 0을 출력
    print(bfs())