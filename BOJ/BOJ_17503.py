from heapq import heappush, heappop
import sys

# 축제가 열리는 기간 N, 선호도의 합 M, 마실 수 있는 맥주 종류의 수 K
N, M, K = map(int, sys.stdin.readline().split())
V = [map(int, sys.stdin.readline().split()) for _ in range(K)]