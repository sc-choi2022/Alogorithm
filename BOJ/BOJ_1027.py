import sys

# 빌딩의 총 개수 N
N = int(sys.stdin.readline())
# 빌딩의 높이를 저장하는 배열 heights
heights = [0] + list(map(int, sys.stdin.readline().split()))
# 보이는 빌딩의 수 answer, 그 빌딩의 번호 number
answer, number = 0, 0