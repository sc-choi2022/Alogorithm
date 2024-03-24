import sys


# 에너지 구슬의 개수 N
N = int(sys.stdin.readline())
# 에너지 구슬을 저장하는 배열 marbles
marbles = list(map(int, sys.stdin.readline().split()))
visit = [0]*N
# 모을 수 있는 에너지의 최댓값 answer
answer = 0