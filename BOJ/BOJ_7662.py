from heapq import heappush, heappop
import sys

# 테스테이스 개수 T
T = int(sys.stdin.readline())

for _ in range(T):
    # 연산의 개수 K
    K = int(sys.stdin.readline())
    # 이중 우선순위 큐 최소 힙 Q1, 최대 힙 Q1
    Q1, Q2 = [], []

    for _ in range(K):
        # 주어지는 연산 O과 정수 N
        O, N = sys.stdin.readline().rstrip().split()

        # 삽입 연산
        if O == 'I':
            heappush(Q1, int(N))
            heappush(Q2, -int(N))
        else:
            if not Q1 or not Q2:
                continue
            # 최댓값 삭제
            elif N == '1':
                heappop(Q2)
            # 최솟값 삭제
            else:
                heappop(Q1)
    print(len(Q1), len(Q2))