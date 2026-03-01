from itertools import combinations
import sys

# 기타의 개수 N, 곡의 개수 M
N, M = map(int, sys.stdin.readline().split())

guitar = []

for _ in range(N):
    name, songs = sys.stdin.readline().rstrip().split()

    bit = 0
    for i in range(M):
        if songs[i] == 'Y':
            bit |= (1 << (M-1-i))
        guitar.append(bit)
    max_s, min_g = 0, -1

    for j in range(1, N+1):
        for com in combinations(guitar, j):
            tmp = 0
            for c in com:
                tmp |= bit
            cnt = bin(tmp).count('1')

            if cnt > max_s:
                max_s = cnt
                min_g = j
if max_s == 0:
    print(-1)
else:
    print(min_g)
