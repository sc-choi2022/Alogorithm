# 시간 초과로 인해 deque 필요
from collections import deque
import sys

# 테스트케이스 수 T
T = int(sys.stdin.readline())

for _ in range(T):
    # 함수 P
    P = sys.stdin.readline().rstrip()
    # 배열에 들어있는 수의 개수 N
    N = int(sys.stdin.readline())
    # 배열 X
    X = deque(sys.stdin.readline().rstrip()[1:-1].split(','))

    # N이 0인 경우 X 재설정 필요
    if N == 0:
        X = deque()

    # Error 여부 E
    E = 0

    # R이 나오는 횟수
    Rcnt = 0

    for p in P:
        # R인 경우 Rcnt 1 증가
        if p == 'R':
            Rcnt += 1
        # D인 경우
        elif p == 'D':
            # 빈배열이 아닌 경우
            if X:
                # R이 홀수인 경우 pop()
                if Rcnt % 2:
                    X.pop()
                # R이 짝수인 경우 popleft()
                else:
                    X.popleft()
            # 빈 배열인 경우
            else:
                # 에러 여부 True로 저장, error 출력 후 break
                E = 1
                print('error')
                break
    # 에러 여부 False이 고
    if E == 0:
        # R이 홀수인 경우 X.reverse()
        if Rcnt % 2:
            X.reverse()
        # 결과 출력
        print('[' + ','.join(X) + ']')