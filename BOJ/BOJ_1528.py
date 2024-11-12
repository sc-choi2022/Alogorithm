from collections import deque
import sys

def gold():
    queue = deque([(N, [])])

    while queue:
        number, tmp = queue.popleft()

        if number == 0:
            print(*sorted(tmp))
            break

        L = len(str(number))

        for i in range(L, 0, -1):
            if int('7'*i) <= number:
                queue.append((number-int('7'*i), tmp + [int('7'*i)]))
            if int('4'*i) <= number:
                queue.append((number-int('4'*i), tmp + [int('4'*i)]))
    else:
        print(-1)

# 정수 N
N = int(sys.stdin.readline())
gold()