import sys

# 2차원 세계의 세로 길이 H, 가로 길이 W
H, W = map(int, sys.stdin.readline().split())
# 블록이 쌓인 높이를 저장하는 배열 heights
heights = list(map(int, sys.stdin.readline().split()))
# 고이는 빗물의 양 water
water = 0

for i in range(1, W-1):
    # 좌측과 우측의 가장 높은 높이 left, right
    left = max(heights[:i])
    right = max(heights[i+1:])
    # 현재 위치와 비교하기 위한 낮은 높이 lower
    lower = min(left, right)
    # 물이 고일 수 있는 경우
    if lower > heights[i]:
        water += lower - heights[i]
# 고이는 빗물의 총량을 출력
print(water)