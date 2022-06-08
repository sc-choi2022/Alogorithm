import sys

# 수의 개수 N, 합을 구해야하는 개수 M
N, M = map(int, sys.stdin.readline().split())

# N개의 숫자를 담은 리스트 num
num = list(map(int, sys.stdin.readline().split()))

# 합이 담긴리스트
sumlist = [0] * (N + 1)
for i in range(1, N+1):
    sumlist[i] = sumlist[i-1] + num[i-1]

for _ in range(M):
    start, end = map(int, sys.stdin.readline().split())
    print(sumlist[end]- sumlist[start-1])