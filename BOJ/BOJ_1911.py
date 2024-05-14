import sys

# 물 웅덩이의 개수 N, 널빤지의 길이 L
N, L = map(int, sys.stdin.readline().split())
# 물 웅덩이의 정보를 저장하는 배열 water
water = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]