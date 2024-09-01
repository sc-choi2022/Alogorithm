import sys

# 물 웅덩이의 개수 N, 널빤지의 길이 L
N, L = map(int, sys.stdin.readline().split())
# 물 웅덩이의 정보를 저장하는 배열 water
water = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
water.sort()
# 필요한 널빤지들의 최소 개수 answer
answer = 0

# 널빤지의 위치를 저장하는 변수 board
board = water[0][0]
for S, E in water:
    if board > E:
        continue
    elif board < S:
        board = S
    # 널빤지로 가려야하는 거리
    gap = E - board
    # 이번 웅덩이를 모두 가리는데 필요한 개수 cnt
    if gap % L:
        cnt = gap // L + 1
    else:
        cnt = gap // L
    board += L * cnt
    answer += cnt

# answer 출력
print(answer)