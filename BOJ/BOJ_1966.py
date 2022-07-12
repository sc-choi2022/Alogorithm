import sys
from collections import deque

# 테스트케이스 T
T = int(sys.stdin.readline())

for _ in range(T):
    # 문서의 개수, 궁금한 문서의 현재 위치 M
    N, M = list(map(int, sys.stdin.readline().split()))
    important = deque(map(int, sys.stdin.readline().split()))
    # 문서마다의 idx을 지정해준다.
    idx = deque(range(len(important)))
    # 확인 문서의 현재 위치의 값을 target으로 수정
    idx[M] = 'target'

    # 출력할 위치를 나타낼 변수 order
    order = 0
    while True:
        # 첫번째 위치가 important의 최댓값이면 order 1 증가
        if important[0] == max(important):
            order += 1
            # idx의 첫번째 값이 target이라면 order 출력
            if idx[0] == 'target':
                print(order)
                break
            else:
                # important와 idx의 첫번째 값을 제거
                important.popleft()
                idx.popleft()
        # important와 idx의 첫값을 다시 맨 뒤로 추가
        else:
            important.append(important.popleft())
            idx.append(idx.popleft())