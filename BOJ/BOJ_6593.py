import sys

while True:
    # 충수 L, 한 층의 행 R, 한 층의 열 C
    L, R, C = map(int, sys.stdin.readline().split())

    if L==0 and R==0 and C==0:
        break
    building = [[] for _ in range(L)]
    for i in range(L):
        lst = [[] for _ in range(R)]
        for j in range(R):
            lst[j] = list(sys.stdin.readline().rstrip())
        blank = sys.stdin.readline().rstrip()
        building[i] = lst