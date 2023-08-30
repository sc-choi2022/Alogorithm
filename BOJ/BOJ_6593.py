import sys

while True:
    # 충수 L, 한 층의 행 R, 한 층의 열 C
    L, R, C = map(int, sys.stdin.readline().split())

    if L==0 and R==0 and C==0:
        break

    building = [[list(sys.stdin.readline().rstrip()) for _ in range(C)] for _ in range(L)]

    # for b in building:
    #     print(*b)