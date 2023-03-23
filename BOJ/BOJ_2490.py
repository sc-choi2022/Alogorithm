import sys

for _ in range(3):
    # 윷의 정보를 담을 배열 bars
    bars = list(map(int, sys.stdin.readline().split()))
    # 배의 개수를 저장할 변수 cnt
    cnt = bars.count(0)

    if cnt == 0:
        print('E')
    elif cnt == 1:
        print('A')
    elif cnt == 2:
        print('B')
    elif cnt == 3:
        print('C')
    else:
        print('D')