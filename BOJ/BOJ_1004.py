import sys

# 테스트 케이스
T = int(sys.stdin.readline())

for _ in range(T):
    # 출력할 횟수 cnt
    cnt = 0
    # 시작점 x1, y1 도착점 x2, y2
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    # 행성계의 개수 N
    N = int(sys.stdin.readline())

    for i in range(N):
        # 행성계의 위치 cx, cy 반지름 r
        cx, cy, r = map(int, sys.stdin.readline().split())
        # 시작점과 행성계의 중심 사이의 거리
        d1 = ((x1-cx)**2 + (y1-cy)**2)**0.5
        # 도착점과 행성계의 중심 사이의 거리
        d2 = ((x2-cx)**2 + (y2-cy)**2)**0.5
        # 도착점과 시작점이 서로 다른 원 안에 있는 경우 진입이나 이탈이 발생
        # 두 길이주 하나만 r보다 작아 원안에 있는 경우 그 원을 벗어나야 하므로 cnt 1 증가
        if (d1 < r and d2 > r) or (d1 > r and d2 < r):
            cnt += 1
    # N개의 행성계를 확인하고 cnt 출력
    print(cnt)