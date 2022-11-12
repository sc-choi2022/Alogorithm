import sys

# 집합S의 크기 L
L = int(sys.stdin.readline())
# 집합 S
S = sorted([0] + list(map(int, sys.stdin.readline().split())))
# 포함해야하는 정수 n
n = int(sys.stdin.readline())

# n이 S에 포함되어 구간이 없는 경우 0 출력 후 break
if n in S:
    print(0)
else:
    for i in range(L):
        # n이 S의 정수들 사이 범위에 포함되는 경우
        if S[i] < n and n < S[i+1]:
            # 구간의 경우의 수를 계산 후 출력
            print((n - S[i]) * (S[i+1] - n) - 1)
            break