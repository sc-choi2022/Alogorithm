import sys

# 플레이어의 수 N, 가진 카드 수 M
N, M = map(int, sys.stdin.readline().split())
cards = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]