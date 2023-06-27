from collections import deque
import sys

# 수빈의의 위치 N, 동생의 위치 K
N, K = map(int, sys.stdin.readline().split())
# 방문할 수 있는 최소 시간을 저장하는 배열 visit
visit = [[-1, 0] for _ in range(100001)]

if N >= K:
    print(N-K)
    print(1)
else:
    queue = deque([N])
    # 방문에 걸리는 시간 0, 방문하는 경우의수 1를 visit배열에 저장
    visit[N][0], visit[N][1] = 0, 1

    while queue:
        current = queue.popleft()

        for next in 2*current, current+1, current-1:
            if 0 <= next <= 100000:
                # 처음 next에 도착한 경우
                if visit[next][0] == -1:
                    visit[next][0] = visit[current][0] + 1 # 걸리는 시간
                    visit[next][1] = visit[current][1] # 경우의 수 저장
                    queue.append(next)
                # 이전에 방문했지만 최단 시간인 경우
                elif visit[next][0] == visit[current][0] + 1:
                    visit[next][1] += visit[current][1]
    # 수빈이가 동생을 찾는 가장 빠른 시간을 출력
    print(visit[K][0])
    # 가장 빠른 시간으로 수빈이가 동생을 찾는 방법의 수를 출력
    print(visit[K][1])