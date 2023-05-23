from collections import deque
import sys

def bfs():
    queue = deque([(N, [N])])
    visit[N] = 1
    # N이 K보다 큰 경우
    if N > K:
        return [x for x in range(N, K-1, -1)]

    while queue:
        site, path = queue.popleft()
        # 동생의 위치에 도달한 경우
        if site == K:
            return path

        for next in 2*site, site-1, site+1:
            if 0 <= next <= 100000 and not visit[next]:
                visit[next] = 1
                queue.append((next, path + [next]))

# 수빈이의 위치 N, 동생의 위치 K
N, K = map(int,sys.stdin.readline().split())

# 방문한 시간을 저장하는 배열 visit
visit = [0] * 200001
# 방문 위치 순서를 answer에 저장
answer = bfs()
# 가장 빠른 시간을 출력
print(len(answer)-1)
# 어떻게 이동해야 하는지 공백으로 구분해 출력
print(*answer)