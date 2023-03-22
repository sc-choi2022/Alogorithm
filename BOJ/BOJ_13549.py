from collections import deque
import sys

def bfs(start):
    queue = deque()
    queue.append(start)

    while queue:
        site = queue.popleft()
        # 동생의 위치에 도착한 경우 수빈이가 동생을 찾는 가장 빠른 시간을 출력
        if site == K:
            print(visit[K])
            break

        # 수빈이가 움직이는 세가지 방법
        for next in (2 * site), (site + 1), (site - 1):
            # next가 범위 안이며 방문하지 않은 위치인 경우
            if 0 <= next < 100001 and visit[next] == -1:
                # 순간이동의 경우
                if next == 2 * site:
                    # visit[next]에 시간 저장하고 queue의 앞에 위치 추가
                    visit[next] = visit[site]
                    queue.appendleft(next)
                # 순간이동이 아닌 경우
                else:
                    # visit[next]에 시간 1증가하여 저장하고 queue의 뒤에 위치 추가
                    visit[next] = visit[site] + 1
                    queue.append(next)


# 수빈이의 위치 N, 동생의 위치 K
N, K = map(int, sys.stdin.readline().split())
# 위치 도착하는 빠른 시간을 담을 배열 visit
visit = [-1] * 100001
# 현재 수빈이의 위치를 visit[N]에 반영
visit[N] = 0
# 수빈이의 위치를 매개변수로 bfs(N) 실행
bfs(N)