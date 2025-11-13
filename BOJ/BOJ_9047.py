from itertools import combinations
import sys

# 테스트 케이스의 개수 T
T = int(sys.stdin.readline())

for _ in range(T):
    # 네자리 수 N
    N = list(map(int, sys.stdin.readline().rstrip()))

    cnt = 0
    while True:
        if int(''.join(N)):
            break
        else:
            n1 = sorted(N, reverse=True)
            n2 = sorted(N)
            result = int(''.join(n1)) - int(''.join(n2))

            N = list(str(result).rstrip())

            if len(N) < 4:
                N = (4-len(N))*['0'] + N
            cnt += 1
    print(cnt)