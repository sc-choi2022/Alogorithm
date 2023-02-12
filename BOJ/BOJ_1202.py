import sys

# 보석의 개수 N, 가방의 개수 K
N, K = map(int, sys.stdin.readline().split())

jewel = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
jewel.sort(key=lambda x: (-x[1], x[0]))

# 가방의 허용무게를 담을 리스트 bags
bags = sorted(list(int(sys.stdin.readline()) for _ in range(K)))
values = [0] * K

for j in jewel:
    for i in range(K):
        if j[0] < bags[i] and values[i] == 0:
            values[i] = j[1]
            break
print(sum(values))