from collections import deque
import sys

# 콩콩의 힘 A, B, 동규의 현재위치 N, 주미의 현재 위치 M
A, B, N, M = map(int, sys.stdin.readline().split())
# 동규가 주미에게 도달하기 위한 최소한의 이동 횟수 answer
answer = 0
# 몇번째 횟수에 i번 돌에 도착하는지를 저장하는 배열 visit
visit = [-1] * 100001
visit[N] = 0

queue = deque([N])
while queue:
    # 동규가 주미에게 도달하기 위한 최소한의 이동 횟수를 출력
    if visit[M] != -1:
        print(visit[M])
        break
    # 현재 위치 current
    current = queue.popleft()
    # 동규가 움직일 수 있는 모든 경우의 for문
    for i in (current*A, current*B, current-A, current-B, current+A, current+B, current-1, current+1):
        # 범위안의 돌이고 미방문했거나 적은 횟수로 방문이 가능한 경우
        if 0 <= i <= 100000 and (visit[i] == -1 or visit[i] > visit[current] + 1):
            visit[i] = visit[current] + 1
            queue.append(i)