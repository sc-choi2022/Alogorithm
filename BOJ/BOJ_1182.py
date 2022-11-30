from itertools import combinations
import sys

# 정수의 개수 N, 정수 S
N, S = map(int, sys.stdin.readline().split())

# 수열을 담을 리스트 sequence
sequence = list(map(int, sys.stdin.readline().split()))

# 합이 S가 되는 부분수열의 개수 cnt
cnt = 0

for i in range(1, N + 1):
    for c in combinations(sequence, i):
        if sum(c) == S:
            cnt += 1
# cnt 출력
print(cnt)