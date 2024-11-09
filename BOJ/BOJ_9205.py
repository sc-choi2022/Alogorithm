from collections import deque
import sys

def bfs():
    global answer

    # 시작 위치와 맥주의 개수로 시작
    queue = deque([(hi, hj)])
    # 편의점의 방문여부를 저장하는 배열 visit
    visit = [0] * N

    while queue:
        # 현재 위치와 맥주의 개수
        ci, cj = queue.popleft()
        # 락 페스티벌에 도착가능한 경우 answer 갱신 후 return
        if (abs(ci-ri) + abs(cj-rj)) / 50 <= 20:
            answer = 'happy'
            return

        for i in range(N):
            ni, nj = CVS[i]
            # 미방문 편의점이고 맥주양으로 도착가능한 경우
            if not visit[i] and (abs(ci-ni) + abs(cj-nj)) / 50 <= 20:
                visit[i] = 1
                queue.append((ni, nj))

# 테스트 케이스 개수 T
T = int(sys.stdin.readline())

for _ in range(T):
    # 편의점의 개수 N
    N = int(sys.stdin.readline())
    # 집의 좌표
    hi, hj = map(int, sys.stdin.readline().split())
    # 편의점의 좌표를 저장하는 배열 CVS
    CVS = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
    # 락 페스티벌 좌표
    ri, rj = map(int, sys.stdin.readline().split())
    answer = 'sad'
    bfs()
    # 행복하게 페스티벌에 갈 수 있으면 happy 출력
    # 중간에 맥주가 바닥나서 더 이동할 수 없으면 sad 출력
    print(answer)