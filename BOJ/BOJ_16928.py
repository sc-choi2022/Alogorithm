import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

# 사다리와 뱀에 따른 위치정보를 담은 game,
# game의 위치의 방문여부를 확인하는 visit,
# game의 위치에 도달가능한 최소 주사위 횟수를 담은 cnt
game = [0] * 101
visit = [0] * 101
cnt = [0] * 101

for _ in range(M + N):
    x, y = map(int, sys.stdin.readline().split())
    game[x] = y

# queue와 visit에 시작 1번 칸을 정보를 반영
queue = deque()
queue.append(1)
visit[1] = 1

while queue:
    place = queue.popleft()

    for i in range(1, 6+1):
        next = place + i
        # 다음 위치 next가 범위 안 위치인 경우
        if next <= 100:
            # 사다리 혹은 뱀으로 인해 위치가 변경된다면 next에 정보 반영
            if game[next]:
                next = game[next]
            # 방문하지 않은 위치인 경우 방문 표시, queue에 추가, cnt에 값 추가
            if visit[next] == 0:
                visit[next] = 1
                queue.append(next)
                cnt[next] = cnt[place] + 1
    # 100번 칸에 도착했다면 cnt[100] 출력 후 break
    if cnt[100]:
        print(cnt[100])
        break