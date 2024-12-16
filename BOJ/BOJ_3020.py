import sys

# 동굴의 길이 N, 높이 H
N, H = map(int, sys.stdin.readline().split())
# 석순과 종유석의 정보를 담은 배열 cave
cave = [int(sys.stdin.readline()) for _ in range(N)]
# 동굴의 높이에 따른 석순과 종유석의 정보를 담을 배열 line
line = [0] * H

for i in range(N):
    length = int(sys.stdin.readline())

    if i%2:
        line[0] += 1
        line[length] -= 1
    else:
        line[H-length] -= 1

M = min(line)
print(M, line.count(M))