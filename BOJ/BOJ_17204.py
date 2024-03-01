from collections import deque
import sys

# 참여하는 사람의 수 N, 보성이의 번호 K
N, K = map(int, sys.stdin.readline().split())

# 지목받는 순서를 저장하는 배열 visit
visit = [-1] * N
visit[0] = 0
# bfs를 활용하기 위한 queue
queue = deque([0])

pick = [[] for _ in range(N)]
for i in range(N):
    # i번 사람이 지목하는 사람의 번호 a
    pick[i].append(int(sys.stdin.readline()))

while queue:
    current = queue.popleft()
    # 보성이가 지목되는 가장 작은 정수 M을 출력
    if visit[K] != -1:
        print(visit[K])
        break

    for choose in pick[current]:
        if visit[choose] == -1:
            visit[choose] = visit[current] + 1
            queue.append(choose)
# 보성이가 걸리지 않는 경우 -1 출력
else:
    print(visit[K])