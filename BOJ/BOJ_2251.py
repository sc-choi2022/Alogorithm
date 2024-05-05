from collections import deque
import sys

# 세 개의 물통의 부피 A, B, C
A, B, C = map(int, sys.stdin.readline().split())
# A와 B의 물 용량을 확인 여부를 저장하는 배열 visit
visit = [[0]*201 for _ in range(201)]
# A와 B의 초기 값을 visit에 저장
visit[0][0] = 1
queue = deque([(0, 0, C)])
# C의 용량을 저장하는 배열
answer = [0]*201

while queue:
    # 현재 물통의 용량 각 cA, cB, cC
    cA, cB, cC = queue.popleft()

    if visit[cA][cB]:
        continue
    visit[cA][cB] = 1

    # 물통 A가 비어 있는 경우
    if cA == 0:
        answer[cC] = 1

    # A -> B
    if cA + cB < B:
        queue.append((0, cA+cB, cC))
    else:
        queue.append((cA+cB-B, B, cC))

    # A -> C
    if cA + cC < C:
        queue.append((0, cB, cA + cC))
    else:
        queue.append((cA+cC-C, cB, C))

    # B -> A
    if cA + cB < A:
        queue.append((cA+cB, 0, cC))
    else:
        queue.append((A, cA+cB-B, cC))

    # B -> C
    if cB + cC < C:
        queue.append((cA, 0, cB+cC))
    else:
        queue.append((cA, cB+cC-C, C))

    # C -> A
    if cA + cC < A:
        queue.append((cA+cC, cB, 0))
    else:
        queue.append((A, cB, cA+cC-C))

    # C -> B
    if cB + cC < C:
        queue.append((cA, cB+cC, 0))
    else:
        queue.append((cA, B, cB+cB-C))

for i in range(201):
    # 세 번째 물통(용량이 C인)에 담겨있을 수 있는 물의 양을 공백으로 구분하여 출력
    if answer[i]:
        print(i, end=' ')