from collections import deque
import sys

# 참여하는 사람의 수 N, 보성이의 번호 K
N, K = map(int, sys.stdin.readline().split())

# 지목받는 순서를 저장하는 배열 visit
visit = [0] * N
visit[0] = 1
# bfs를 활용하기 위한 queue
queue = deque([0])

pick = [[] for _ in range(N)]
for i in range(N):
    # i번 사람이 지목하는 사람의 번호 a
    pick[i] = int(sys.stdin.readline())

while queue:
    current = queue.popleft()