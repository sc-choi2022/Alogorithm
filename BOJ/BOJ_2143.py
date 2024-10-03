from collections import defaultdict
import sys

# 목표 합 T
T = int(sys.stdin.readline())
# 배열 A의 크기 N
N = int(sys.stdin.readline())
# 배열 A
A = list(map(int, sys.stdin.readline().split()))
# 배열 B의 크기 M
M = int(sys.stdin.readline())
# 배열 B
B = list(map(int, sys.stdin.readline().split()))

# 배열 A의 부 배열의 합의 정보를 저장하는 딕셔너리 SA
SA = defaultdict(int)
for i in range(N):
    tmpA = A[i]
    SA[tmpA] += 1
    for j in range(i+1, N):
        tmpA += A[j]
        SA[tmpA] += 1

# 부 배열 쌍의 개수 answer
answer = 0
for ii in range(M):
    tmpB = B[ii]

    if SA[T-tmpB]:
        answer += SA[T-tmpB]
    for jj in range(ii+1, M):
        tmpB += B[jj]
        if SA[T-tmpB]:
            answer += SA[T-tmpB]
# answer 출력
print(answer)