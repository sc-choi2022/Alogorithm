# from itertools import permutations
# import sys
#
# # 배열 A의 정수 개수 N
# N = int(sys.stdin.readline())
# # 배열 A
# A = list(map(int, sys.stdin.readline().split()))
# # 모든 경우의 수를 담는 배열 permu
# permu = list(permutations(A, N))
# # 최댓값을 담을 변수 ans
# ans = 0
#
# for p in permu:
#     tmp = 0
#     for i in range(1, N):
#         tmp += abs(p[i] - p[i-1])
#     ans = max(ans, tmp)
# print(ans)

import sys

# 재쉬함수로 순열하는 함수 permu
def permu(lst):
    global ans

    if len(lst) == N:
        tmp = 0
        for i in range(1, N):
            tmp += abs(lst[i] - lst[i-1])
        ans = max(ans, tmp)
        return

    for j in range(N):
        if visit[j] == 0:
            visit[j] = 1
            lst.append(A[j])
            permu(lst)
            visit[j] = 0
            lst.pop()

# 배열 A의 정수 개수 N
N = int(sys.stdin.readline())
# 배열 A
A = list(map(int, sys.stdin.readline().split()))
# 확인을 위한 배열 visit
visit = [0] * N
# 최댓값을 담을 변수 ans
ans = 0
# []를 매개변수로 permu을 실행
permu([])
print(ans)