import sys

while True:
    # 상근이가 가지고 있는 CD의 수 N, 선영이가 가지고 있는 CD의 수 M
    N, M = map(int, sys.stdin.readline().split())

    if (N, M) == (0, 0):
        break

    # 상근이가 가진 CD의 번호를 저장하는 셋 cnt
    cnt = set(int(sys.stdin.readline()) for _ in range(N))

    for _ in range(M):
        CD = int(sys.stdin.readline())
        if CD in cnt:
            cnt.remove(CD)

    # 두 사람이 동시에 가지고 있는 CD의 개수를 출력
    print(N-len(cnt))