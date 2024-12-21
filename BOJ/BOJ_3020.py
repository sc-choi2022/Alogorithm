import sys

# 동굴의 길이 N, 높이 H
N, H = map(int, sys.stdin.readline().split())
# 동굴의 높이에 따른 석순과 종유석의 정보를 담을 배열 line
line = [0] * H

for i in range(N):
    length = int(sys.stdin.readline())

    # 종유석인 경우
    if i%2:
        line[H-length] += 1
    # 석순인 경우
    else:
        line[0] += 1
        line[length] -= 1

for j in range(1, H):
    line[j] += line[j-1]

# 파괴해야하는 장애물의 최솟값 M
M = min(line)
# 파괴해야 하는 장애물의 최솟값과 그러한 구간의 수를 출력
print(M, line.count(M))