import sys

# 테스트 케이스 수
T = int(sys.stdin.readline())

for _ in range(T):
    # 적군 진영의 숫자 N
    N = int(sys.stdin.readline())
    lst = [[0, 0, 0] for _ in range(N)]
    for i in range(N):
        lst[i] = list(map(int, sys.stdin.readline().split()))