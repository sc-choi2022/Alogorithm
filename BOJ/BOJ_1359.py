from itertools import combinations
import sys

# 1부터 N까지의 수 중에 서로 다른 M개의 수를 골라 적어도 K개의 수가 같으면 당첨
# 정수 N, M, K
N, M, K = map(int, sys.stdin.readline().split())

C = combinations([x for x in range(N)], M)
win = 0

for c in C:
    cnt = 0
    for i in range(M):
        if c[i] < M:
            cnt += 1
        if cnt >= K:
            win += 1

# 당첨 확률 출력
print(win/len(list(C)))