import sys

# 배열A의 크기 N
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
# 교환 횟수 S
S = int(sys.stdin.readline())

for i in range(N):
    max_num = max(A[i: min(N, i + S + 1)])
    idx = A.index(max_num)

    for j in range(idx, i, -1):
        A[j], A[j - 1] = A[j - 1], A[j]
    S -= (idx - i)
    if S <= 0:
        break

print(*A)